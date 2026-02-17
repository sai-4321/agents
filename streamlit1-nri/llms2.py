import streamlit as st
from google import genai

client = genai.Client(api_key="AIzaSyCtontFEOCb9ykNM6cw7c4R6I5zuBDSd38")

text_user = st.chat_input("enter your prompt")

if text_user:
    # create a fresh list every run
    messages = []

    messages.append({
        "role": "user",
        "content": text_user
    })

    with st.spinner("loading..."):
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=text_user
        )

    messages.append({
        "role": "assistant",
        "content": response.text
    })

    st.write(messages)
