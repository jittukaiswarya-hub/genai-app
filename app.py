import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# App title
st.title("🛍️ AI Marketing Copy Generator")

# Input fields
product = st.text_input("Enter Product Name:")
features = st.text_area("Enter Product Features (one per line):")

# Button to generate marketing copy
if st.button("Generate Marketing Copy"):
    prompt = f"""
    Convert the following product specs into attractive marketing copy.

    Product: {product}
    Features:
    {features}

    Make it engaging and persuasive.
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("✨ Marketing Copy:")
    st.write(response.choices[0].message.content)