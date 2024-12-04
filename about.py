import streamlit as st

def about_page():
    # Set a light gradient background using CSS
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffad60, #ffff99, #a8e6cf);  /* Soft light blue to purple gradient */
    }

    /* Apply font family and size changes globally */
    body {
        font-family: 'Arial', sans-serif;  /* You can replace 'Arial' with any other font */
        font-size: 25px;  /* Adjust the font size */
        line-height: 1.6;  /* Optional: improves readability */
    }

    /* Additional styling for the title */
    .stTitle {
        font-size: 30px;  /* Adjust the title size */
        font-family: 'Arial', sans-serif;  /* Match the title font with the body */
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.title("About")

    # Main content
    st.write("""
    'AI at Your Fingertips' is a platform that brings the power of deep learning directly to you. 
    With our selection of five unique AI models, you can interact with and explore the boundaries of technology in exciting new ways.
    - **Whisper Wave:** Converts audio to text.
    - **Sound Synths:** Generates music from text.
    - **Chat with Qwen:** Offers interactive conversations.
    - **AI Vision to Text:** Interprets images into text.
    - **Prompted Realities:** Allows you to generate stunning images from your descriptions.

    Whether you're a developer, designer, or just curious about AI, our platform is here to help you unlock new creative possibilities.
    """)


