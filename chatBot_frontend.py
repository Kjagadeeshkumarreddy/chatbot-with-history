import streamlit as st
from langchain_core.messages import HumanMessage
from chatBot_backend import chatbot, retrive_all_threads
import uuid

def generate_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('message', [])

# Initialize session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state or st.session_state['chat_threads'] is None:
    threads = retrive_all_threads()
    st.session_state['chat_threads'] = threads if threads else []

add_thread(st.session_state['thread_id'])

# Sidebar
st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")
for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_message = []
        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_message.append({'role': role, 'content': msg.content})
        st.session_state['message_history'] = temp_message

# Main UI
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.write(message['content'])

user_input = st.chat_input('Type here', key=f"chat_input_{st.session_state['thread_id']}")
if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {"thread_id": st.session_state["thread_id"]},
        "run_name": "chat_turn",
    }

    with st.chat_message('assistant'):
        response_chunks = chatbot.stream(
            {'message': [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        )
        ai_message = ""
        placeholder = st.empty()
        for message_chunk, metadata in response_chunks:
            cleaned = message_chunk.content.replace("<think>", "").replace("</think>", "")
            # Preserve original message spacing between chunks
            ai_message += cleaned
            placeholder.write(ai_message)

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
