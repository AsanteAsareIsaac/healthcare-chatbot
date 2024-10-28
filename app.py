import streamlit as st

# Function to define the main app
def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Healthcare Chatbot",
        page_icon="💬",
        layout="wide",
    )

    # Sidebar for navigation or information
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3820/3820330.png", width=100)  # Adding a logo to the sidebar
    st.sidebar.title("Chatbot Information")
    st.sidebar.markdown("""
        Welcome to the Healthcare Chatbot! 💡
        
        Ask me anything related to your health, and I'll do my best to help.
        
        **Note:** This is a demo, and responses are not medical advice.
    """)

    # Main header and introduction
    st.markdown("<h1 style='text-align: center;'>Healthcare Chatbot 🤖</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 18px;">
                Hello! I'm your virtual healthcare assistant. <br>
                I can help answer your questions about health-related topics.<br>
                Just type your question below and I'll do my best to assist you!
            </p>
        </div>
    """, unsafe_allow_html=True)

    # User input section with centered layout
    st.markdown("<h2 style='text-align: center;'>Ask Your Question</h2>", unsafe_allow_html=True)
    
    # Center-align the input text box
    user_input = st.text_input("", placeholder="Ask a health question...", key="user_input")

    # Center the Send button using CSS
    st.markdown(
        """
        <div style='display: flex; justify-content: center;'>
            <button class='send-button' onclick="Streamlit.setComponentValue('user_input')">Send</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add a button to simulate sending the message in Python logic
    if st.button("Send", key="send_button"):
        if user_input:
            st.success("Your question has been sent! (This is a demo, so no model response.)")
            # Placeholder for model response (to be connected later)
            st.markdown("**Response:** This will be the response from the chatbot model.")
        else:
            st.warning("Please enter a question before sending.")

    # Footer section for additional information or disclaimers
    st.markdown("""
        <hr style="border-top: 1px solid #eee;" />
        <div style="text-align: center;">
            <h4>Disclaimer</h4>
        <p>
            This chatbot is currently in a testing phase and will soon be connected to a model endpoint for accurate results.
        </p>
        </div>
    """, unsafe_allow_html=True)

    # Adding some custom styling for better visuals
    st.markdown(
        """
        <style>
        .stTextInput {
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton button {
            display: none; /* Hide default Streamlit button */
        }
        .send-button {
            background-color: #4CAF50; /* Green */
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
        .send-button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Run the Streamlit app
if __name__ == "__main__":
    main()
