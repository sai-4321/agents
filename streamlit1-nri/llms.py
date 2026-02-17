import streamlit as st
from google import genai
 # it is code with session state
if "message" not in st.session_state:
    st.session_state.message=[]


text_user=st.chat_input("enter your prompt")

if text_user:
    st.session_state.message.append({"role":"user","content":text_user})
    client = genai.Client(api_key="AIzaSyCtontFEOCb9ykNM6cw7c4R6I5zuBDSd38")
    with st.spinner("loading........"):
      response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=text_user        
      )
#st.write(response.text)
st.session_state.message.append({"role":"assistant","content":response.text}) 

for i in st.session_state.message:
   with st.chat_message(i["role"]):
        #with st.expander(i["role"]):
        st.write(i["content"])
   
#st.write(st.session_state.message)
  #  [ {
  #       "role":"user",
  #       "content":text_user
  #               },
  #    {
  #        "role":"assistant",
  #        "content":genai-res
                    
  #               }]

    

# data=st.text_input("enter prompt")
# btn=st.button("submit")
# if btn:
#    #st.write(data)
#    client = genai.Client(api_key="AIzaSyCtontFEOCb9ykNM6cw7c4R6I5zuBDSd38")
#    with st.spinner("loading........"):
#     response = client.models.generate_content(
#        model="gemini-3-flash-preview", contents=data
#        #"Explain how AI works in a few words"
# )
#st.write(response.text)