import streamlit as st

st.title("Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate assistant response
    response = f"Echo: {prompt}"  # Simple echo response
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to show the updated messages immediately
    st.rerun()

from streamlit.web import cli as stcli
from streamlit import runtime
import sys

if __name__ == '__main__':
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
