import streamlit as st
import requests

# Function to interact with the FastAPI backend
def get_ai_response(user_input):
    """
    Send user input to the backend API and return the AI-generated response.
    """
    try:
        # Send POST request to the backend API
        response = requests.post(
            "https://fast-api-application.onrender.com/chain/invoke",
            json={
                "input": {
                    "user_input": user_input
                },
                "config": {},
                "kwargs": {}
            },
        )

        # Check if the response is successful
        if response.status_code == 200:
            # Parse the response JSON to extract the AI's reply
            return response.json().get("output", "No response received from the AI.")
        else:
            return f"Error: Backend returned status code {response.status_code}"
    except Exception as e:
        return f"Error: Unable to connect to the backend. Details: {e}"

# Main function for Streamlit chatbot application
def main():
    # Set Streamlit page configuration
    st.set_page_config(page_title="Healthcare Chatbot", page_icon="💬", layout="wide")

    # Sidebar for navigation or branding
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3820/3820330.png", width=100)
    st.sidebar.title("Chatbot Information")
    st.sidebar.markdown("""
        Welcome to the Healthcare Chatbot! 💡
        
        Ask me anything related to your health, and I'll do my best to help.
        
        **Note:** This chatbot is for informational purposes only and not a substitute for professional medical advice.
    """)

    # Main chatbot interface
    st.title("Healthcare Chatbot 🤖")

    # Session state to maintain chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display existing chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.markdown(message["content"])
        elif message["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(message["content"])

    # User input section
    if user_input := st.chat_input("Type your question here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user message in the chat interface
        with st.chat_message("user"):
            st.markdown(user_input)

        # Send user input to the backend and get the AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                ai_response = get_ai_response(user_input)
                st.markdown(ai_response)

        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Run the Streamlit app
if __name__ == "__main__":
    main()
