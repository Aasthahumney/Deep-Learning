import streamlit as st
import requests


# Define the Hugging Face API URL and your Authorization token
API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": "Bearer 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"}

# Function to call Hugging Face API and get audio
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Function for the music page
def music_page():
    st.markdown(
        """
        <style>
        .stApp {
            background: #a8d0e6;
            animation: waveMove 5s ease-in-out infinite;
        }
        
        @keyframes waveMove {
            0% { transform: translateY(0); }
            50% { transform: translateY(20px); }
            100% { transform: translateY(0); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("SoundSynth: Your Personal AI Composer")
    st.write(
        """
        **SoundSynth** is an AI-powered audio generator that creates high-quality music based on text prompts. Simply provide a description of the type of sound or music you’d like to hear, and the model will generate audio tailored to your preferences. Whether you're looking for ambient soundscapes, upbeat beats, or atmospheric synths, SoundSynth can bring your ideas to life.

        **Example prompts**:
        - "liquid drum and bass, atmospheric synths"
        - "chill lo-fi beats, soft piano"
        - "upbeat pop, electronic rhythms"
        """
    )

    st.write("Enter your prompt below to start creating your own music! (e.g., 'liquid drum and bass, atmospheric synths'):")

    # Text input for user to describe the audio they want
    user_input = st.text_input("Describe your audio:")

    # When user submits the prompt
    if user_input:
        st.write("Generating audio...")

        # Get audio from Hugging Face model
        audio_bytes = query({"inputs": user_input})

        # Display the audio player in Streamlit
        st.audio(audio_bytes, format="audio/wav")

