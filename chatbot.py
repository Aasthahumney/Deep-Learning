import streamlit as st
from huggingface_hub import InferenceClient

# Initialize Hugging Face Inference Client
api = "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"  # Replace with your API key
client = InferenceClient(api_key=api)

# Function for the bot page
def bot_page():
    st.markdown(
    """
    <style>
    /* Animated color-changing gradient background */
    .stApp {
        background: linear-gradient(145deg, #d9b3ff, #b3ffd9, #ffcc80);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }

    /* Gradient shift animation keyframes */
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        25% { background-position: 100% 50%; }
        50% { background-position: 0% 100%; }
        75% { background-position: 100% 100%; }
        100% { background-position: 0% 50%; }
    }

    /* Set text color to white for better contrast */
    h1, h2, div {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.title("Ask Qwen: Your Virtual Assistant")

    st.write("Experience seamless and intelligent conversations with our AI-powered chatbot. Ask anything, and get instant, insightful responses, powered by the latest Hugging Face model—Qwen 2.5.")

    # Chat interface
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat messages
    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input
    if prompt := st.chat_input("Ask me anything!"):
        # Append user message
        st.session_state["messages"].append({"role": "user", "content": prompt})

        # Call Hugging Face API
        with st.spinner("Thinking..."):
            try:
                completion = client.chat.completions.create(
                    model="Qwen/Qwen2.5-Coder-32B-Instruct",
                    messages=st.session_state["messages"],
                    max_tokens=500
                )
                # Extract response
                response_content = completion.choices[0].message["content"]

                # Append assistant message
                st.session_state["messages"].append({"role": "assistant", "content": response_content})

                # Display assistant message
                st.chat_message("assistant").write(response_content)

            except Exception as e:
                st.error(f"Error: {e}")

