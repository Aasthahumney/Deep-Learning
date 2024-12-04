import streamlit as st
import os  # For running external scripts

def home_page():
    # Custom CSS for background animation
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
                color: white;
                font-family: Arial, sans-serif;
                animation: gradientBG 15s ease infinite;
                height: 100vh;
            }
            @keyframes gradientBG {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }
            .stApp {
                background: none;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and header
    st.title("AI at Your Fingertips: Explore the Power of Deep Learning")
    st.write(
        "Welcome to your AI showcase! Dive into cutting-edge models that redefine interaction. "
        "AI at Your Fingertips' integrates five cutting-edge AI models to offer a comprehensive platform for text, image, and audio transformation. Aimed at making deep learning accessible and fun!"
    )

    # Display the models
    st.subheader("Let the sidebar guide you to endless possibilities.")

    st.write("---")
    st.caption("Powered by Streamlit and Hugging Face - Built for innovation.")