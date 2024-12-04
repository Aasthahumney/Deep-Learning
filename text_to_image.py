import streamlit as st
from huggingface_hub import InferenceClient

# Initialize the Hugging Face client
client = InferenceClient("black-forest-labs/FLUX.1-dev", token="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")

# Function for the image generation page
def image_page():
    # Streamlit app styling
    st.markdown(
        """
        <style>
        .stApp {
            background: #d9b3ff;
            animation: rippleEffect 10s linear infinite;
        }
        
        @keyframes rippleEffect {
            0% { background: #d9b3ff; }
            50% { background: #ffffb3; }
            100% { background: #d9b3ff; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Prompted Realities")

    st.markdown(
        """
        Enter a creative text prompt, and watch your imagination come to life with stunning AI-generated images. This app leverages the power of Hugging Face's cutting-edge model, FLUX.1-dev, to transform your words into captivating visuals. Whether you're seeking inspiration, creating art, or just having fun, this tool is your gateway to AI-driven creativity.
        """
    )

    # Input box for the user to enter a prompt
    prompt = st.text_input("Enter a text prompt:", value="Astronaut riding a horse")

    # Button to trigger the image generation
    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                try:
                    # Generate the image using the Hugging Face model
                    image = client.text_to_image(prompt)
                    
                    # Display the generated image
                    st.image(image, caption=f"Generated for: {prompt}", use_container_width=True)
                except Exception as e:
                    st.error(f"Error generating image: {e}")
        else:
            st.warning("Please enter a prompt to generate an image.")
