import streamlit as st
import requests
import sounddevice as sd
import numpy as np
import wave
import tempfile

# Define API URL and headers
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": "Bearer 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"}

# Function to send audio to Hugging Face API
def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# Function to record audio using the microphone
def record_audio(duration=10, fs=16000):
    st.write("Recording... Please speak into your microphone.")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    st.write("Recording complete.")
    
    # Save the audio to a temporary WAV file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    with wave.open(temp_file, 'wb') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(2)  # 16-bit samples
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())
    
    return temp_file.name

# Function for the audio page
def audio_page():
    # Streamlit UI setup
    st.title("WhisperWave: Seamlessly Transforming Speech to Text")
    st.write(""" 
    The **Whisper** model by **OpenAI** is a state-of-the-art speech recognition system. It is designed to transcribe audio into text with high accuracy, even for multiple languages, various accents, and background noise. 
    This model works by processing audio data through a deep learning algorithm that is trained on a vast dataset of diverse spoken language. It performs well in both noisy environments and with different languages, offering robust transcriptions.

    In this app, you can upload an audio file to get a transcription in real-time.
    """)

    # Combined CSS with gradient and wave animation
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(45deg, #ffa552, #f49fb2, #80e7ff, #80b3ff);
            background-size: 200% 200%;
            animation: rotateGradient 8s linear infinite;
        }

        @keyframes rotateGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("Upload an audio file below to get a transcription:")

    # Upload file section
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_uploaded_file = tempfile.NamedTemporaryFile(delete=False)
        with open(temp_uploaded_file.name, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # Process the uploaded file
        st.write(f"Uploaded file: {uploaded_file.name}")
        st.audio(uploaded_file, format="audio/wav")  # Display the uploaded audio
        st.write("Transcribing the uploaded audio...")
        result = query(temp_uploaded_file.name)
        
        # Display transcription
        if 'text' in result:
            st.subheader("Transcription:")
            st.write(result['text'])
        else:
            st.write("Sorry, the transcription failed. Please try again.")
    else:
        st.info("Recording is disabled in this deployed version. Please upload an audio file.")
