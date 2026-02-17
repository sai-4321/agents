import streamlit as st

filee=st.file_uploader("upload a file",type=["png","pdf","jpeg","mp3"])

if filee:
    st.write(filee.type)
    if filee.type.startswith("image"):
     st.image(filee,width=300)
