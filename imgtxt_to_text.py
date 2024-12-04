import streamlit as st
from huggingface_hub import InferenceClient
import requests
from PIL import Image
from io import BytesIO


# Set your Hugging Face API key
api_key = "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"

# Initialize the Hugging Face Inference client
client = InferenceClient(api_key=api_key)

# Function for the vision page
def vision_page():
    st.title("Vision Meets Language: Image & Prompt Magic")
    st.markdown("""
        The **Meta Llama 3.2 Vision-Instruct** model is a cutting-edge AI model by Hugging Face that combines vision and language processing. 
        This model is designed to understand and generate text based on visual inputs. It can analyze an uploaded image and respond to specific prompts by providing descriptions, insights, and other text-based information. 
        Whether you're looking to generate captions, ask questions about an image, or simply get a summary, this powerful AI model brings vision and text together for an interactive experience.
    """)
    st.markdown("**Upload an image and provide a prompt for the model.**")

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #ffcc80;
            animation: colorFade 10s ease infinite;
        }
        
        @keyframes colorFade {
            0% { background-color: #ffcc80; }
            50% { background-color: #80b3ff; }
            100% { background-color: #ffcc80; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # File uploader for image
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    # Text input for the prompt
    user_prompt = st.text_input("Enter a prompt (e.g., 'Describe this image in one sentence.')")

    # Process and display the response
    if st.button("Generate Response"):
        if uploaded_image and user_prompt:
            # Display the uploaded image
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            # Re-encode the image in a standard format
            try:
                buffer = BytesIO()
                image.save(buffer, format="PNG")
                buffer.seek(0)
                
                # Upload the image to a temporary URL
                response = requests.post(
                    "https://file.io/?expires=1d",
                    files={"file": ("image.png", buffer, "image/png")},
                )
                response_data = response.json()
                if not response_data.get("success"):
                    st.error("Failed to upload image to temporary hosting.")
                    st.stop()
                
                image_url = response_data["link"]
            except Exception as e:
                st.error(f"Error processing image: {e}")
                st.stop()
            
            # Prepare the message for the model
            messages = [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": image_url}},
                    ],
                }
            ]
            
            try:
                # Call the Hugging Face model
                st.info("Sending request to Hugging Face model...")
                completion = client.chat.completions.create(
                    model="meta-llama/Llama-3.2-11B-Vision-Instruct",
                    messages=messages,
                    max_tokens=500,
                )

                # Extract the content from the response
                model_response = completion.choices[0].message["content"]

                # Display the response as normal text
                st.success("Model Response:")
                st.write(model_response)
            except Exception as e:
                st.error(f"Error interacting with model: {e}")
        else:
            st.warning("Please upload an image and enter a prompt.")

