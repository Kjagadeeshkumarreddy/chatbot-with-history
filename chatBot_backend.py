from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from langgraph.graph.message import add_messages
import os
from dotenv import load_dotenv
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
import re

# Load environment variables
load_dotenv()

# Use a valid Groq model name — check your Groq dashboard for available models
llm = ChatGroq(model="qwen/qwen3-32b", api_key=os.getenv("GROQ_API"))

class Chat_State(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]

def _extract_name_from_history(messages):
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            text = msg.content.strip().lower()
            if "my name is" in text:
                name = msg.content.strip()[msg.content.lower().index("my name is") + len("my name is"):].strip(" .!\n")
                if name:
                    return name
            if "i am" in text:
                name = msg.content.strip()[msg.content.lower().index("i am") + len("i am"):].strip(" .!\n")
                if name:
                    return name
    return None


def _extract_role_from_history(messages):
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            text = msg.content.strip().lower()
            if "my role is" in text:
                role = msg.content.strip()[msg.content.lower().index("my role is") + len("my role is"):].strip(" .!\n")
                if role:
                    return role
            if "i am a" in text or "i am an" in text:
                for prefix in ["i am a", "i am an"]:
                    if prefix in text:
                        role = msg.content.strip()[msg.content.lower().index(prefix) + len(prefix):].strip(" .!\n")
                        if role:
                            return role
    return None


def _make_concise_message_array(messages):
    if any(isinstance(m, SystemMessage) for m in messages):
        return messages
    return [SystemMessage(content="Answer directly and concisely. Do not include internal thinking, reasoning steps, or explanation of the thought process. Avoid any preambles like 'Okay, the user asked...'. Provide final user-facing text only."), *messages]


def _sanitize_response_text(text: str) -> str:
    cleaned = text.replace("<think>", "").replace("</think>", "").strip()
    # Remove explicit reasoning-style prefixes that should not be visible to the user.
    cleaned = re.sub(r"^Okay,\s*the user asked[\s\S]*?(?:\.\s|\?|!\s)+", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^Okay,\s*the user asked[\s\S]*?\bNow\b[\s]*", "", cleaned, flags=re.IGNORECASE)
    # If there is any present reason text in the first sentence, try to drop it until the first actual answer phrase.
    for seps in ["Your role is", "Your name is", "The answer is", "I think", "I should"]:
        idx = cleaned.lower().find(seps.lower())
        if idx != -1:
            cleaned = cleaned[idx:]
            break
    # keep only the first line for concise output (for non-question prompts this also avoids multiline internal reasoning)
    if "\n" in cleaned:
        cleaned = cleaned.splitlines()[0].strip()
    return cleaned


def chat_model(state: Chat_State):
    message = state["message"]
    if not message:
        return {"message": []}

    # direct user intent handler: name query
    last_user = next((m for m in reversed(message) if isinstance(m, HumanMessage)), None)
    if last_user and "what is my name" in last_user.content.lower():
        known_name = _extract_name_from_history(message[:-1])
        if known_name:
            assistant_response = HumanMessage(content=known_name)
            return {"message": message + [assistant_response]}
        assistant_response = HumanMessage(content="I don't know your name yet. Please tell me!")
        return {"message": message + [assistant_response]}

    if last_user and "what is my role" in last_user.content.lower():
        known_role = _extract_role_from_history(message[:-1])
        if known_role:
            assistant_response = HumanMessage(content=known_role)
            return {"message": message + [assistant_response]}
        assistant_response = HumanMessage(content="I don't know your role yet. Please tell me!")
        return {"message": message + [assistant_response]}

    response = llm.invoke(_make_concise_message_array(message))
    if hasattr(response, "content") and isinstance(response.content, str):
        cleaned = _sanitize_response_text(response.content)
        if last_user and last_user.content.strip().endswith("?"):
            # keep only first sentence for directness
            parts = re.split(r'(?<=[.!?])\s+', cleaned)
            if parts:
                cleaned = parts[0]
        response.content = cleaned
    return {"message": message + [response]}


# SQLite checkpointer
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# Build graph
graph = StateGraph(Chat_State)
graph.add_node("chat_node", chat_model)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def retrive_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None) or []:
        try:
            thread_id = checkpoint.config["configurable"]["thread_id"]
            all_threads.add(thread_id)
        except (AttributeError, KeyError, TypeError):
            continue
    return list(all_threads)
