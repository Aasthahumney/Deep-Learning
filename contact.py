import streamlit as st

# Function to display Contact page
def contact_page():
    # Set a light gradient background using CSS
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e0c3fc, #8ec5fc);  /* Soft gradient from light purple to blue */
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the page
    st.title("Contact")

    # Main content
    st.write("""
    For more information, reach out to me via email:
    - **Email:** mat23ak.humney@pg.ictmumbai.edu.in 

    I'm happy to connect and assist with any inquiries or collaborations!
    """)

    st.write("---")
    st.caption("Powered by Streamlit and Hugging Face - Built for innovation.")

