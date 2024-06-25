import asyncio
import streamlit as st
from run import RAG

# Initialize session state variables
st.session_state.clicked = False
vectorstore_created = False

def get_or_create_eventloop():
    try:
        return asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop

# Set the event loop
loop = get_or_create_eventloop()

@st.cache_resource(show_spinner=True)
def load_rag_pipeline(web_path):
    return RAG(web_path)

# App title and description
st.title("End to End RAG")
st.subheader("An end-to-end RAG pipeline from Document Loading to Monitoring Pipeline")

# Input for website URL
web_path = st.sidebar.text_input("Enter website URL")
if web_path:
    rag_pipe = load_rag_pipeline(web_path)
    st.session_state.clicked = True

# Input for question and display output if URL is provided
if st.session_state.clicked:
    question = st.text_input("Enter your question")
    if question:
        out, vs = rag_pipe.qa(question, vectorstore_created)
        vectorstore_created = vs
        st.write(out)
