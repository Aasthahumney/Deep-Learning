import streamlit as st
from chatbot import bot_page
from audio_to_text import audio_page
from imgtxt_to_text import vision_page
from music_gen import music_page
from text_to_image import image_page
from home import home_page
from contact import contact_page
from about import about_page

def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", 
                                      "Whisper Wave", 
                                      "Chat with Qwen", 
                                      "AI Vision-Text",
                                      "Sound Synths", 
                                      "Prompted Realities",
                                      "About",
                                      "Contact"])

    # Adding custom CSS
    st.markdown("""
        <style>
            .big-font {
            font-size: 3rem;
            color: yellow;
            font-weight: 800;
            cursor: pointer;
            transition: 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)

    # Load the appropriate page based on sidebar selection
    if page == "Home":
        st.markdown('<h1 class="big-font">Welcome to Home Page</h1>', unsafe_allow_html=True)
        home_page()
    
    elif page == "Whisper Wave":
        audio_page()
    
    elif page == "Chat with Qwen":
        bot_page()
    
    elif page == "AI Vision-Text":
        vision_page()
    
    elif page == "Sound Synths":
        music_page()
    
    elif page == "Prompted Realities":
        image_page()

    elif page == "About":
        about_page()
    
    elif page == "Contact":
        contact_page()

if __name__ == "__main__":
    main()
