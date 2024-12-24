import streamlit as st
from backend import generate_response  # Import the backend function

# Title and description
st.title("Chatbot Application")
st.markdown("This is a simple chatbot interface built using Streamlit.")

# Initialize session state for chat log
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Input text box and submit button
user_input = st.text_input("Type your message:", key="input_box")
if st.button("Send"):
    if user_input.strip() == "":
        st.error("Please enter a message.")
    else:
        # Add user input to the chat log
        st.session_state.chat_log.append({"user": user_input, "bot": "Thinking..."})  # Placeholder

        # Generate a response using the backend function
        try:
            bot_response = generate_response(user_input)
            # Replace the placeholder with the actual bot response
            st.session_state.chat_log[-1]["bot"] = bot_response
        except Exception as e:
            st.session_state.chat_log[-1]["bot"] = "Error: Unable to process your request."
            st.error(f"An error occurred: {e}")

# Chat display area
st.write("### Chat Log:")
for chat in st.session_state.chat_log:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
