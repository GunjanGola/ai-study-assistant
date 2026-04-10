import os
import streamlit as st
from groq import Groq

# Add your Groq API key here
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# UI
st.set_page_config(page_title="AI Study Assistant", layout="centered")

st.title("📚 AI Study Assistant")
st.caption("Powered by Groq (fast AI)")

topic = st.text_input("Enter a topic")

if st.button("Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "user",
                            "content": f"Explain {topic} in simple terms and then create 3 quiz questions with answers."
                        }
                    ]
                )

                result = response.choices[0].message.content

                st.subheader("📖 Explanation & Quiz")
                st.write(result)

            except Exception as e:
                st.error(f"Error: {e}")