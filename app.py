import os
import google.generativeai as genai
import streamlit as st

# 1. Setup the Web Page Layout
st.set_page_config(page_title="Nagpur AI Marketing Assistant", page_icon="🍊", layout="centered")

# 2. Configure the Gemini API Key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

# 3. Define the System Instructions
system_instruction = (
    "You are a specialized Gen AI Marketing Assistant built for small business owners in Nagpur, India. "
    "Your job is to help local shops create digital marketing posts, slogans, and product descriptions. "
    "Always offer your responses in a clear layout, providing options in English, Hindi, and Marathi "
    "to cater to the local Vidarbha audience. Keep your tone encouraging, professional, and culturally relevant."
)

# 4. Initialize the Gemini Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_instruction
)

# 5. Build the Web Interface Layout (UI)
st.title("🍊 Nagpur Small Business AI Assistant")
st.subheader("Create local marketing material instantly in English, Hindi, & Marathi")
st.write("Designed for the Google Cloud Gen AI Academy Challenge")

# User Input Text Box on the Web Page
user_prompt = st.text_area(
    "What kind of marketing help do you need today?",
    placeholder="e.g., Write a WhatsApp message to sell fresh Sitabuldi clothing items..."
)

# Clickable Button
if st.button("Generate Marketing Post"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Gemini is crafting your posts..."):
            try:
                # Call the API securely using a state-changing POST pattern
                response = model.generate_content(user_prompt)
                
                st.success("Generated Options successfully!")
                st.markdown("### 📋 Your Marketing Content Layout")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Error connecting to Gemini API: {e}")
