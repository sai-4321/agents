import streamlit as st
import requests as req
from google import genai


st.title("weather suggestion app")

def api_data(city):
       
       url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f9006f6ab25c63ab8a7f1885398cd55a"
       dataa=req.get(url)
       return dataa.json()
def llm_call(data):

 client = genai.Client(api_key="AIzaSyCZbZD3-LpEgonyvKZEXNN4TVReT2D5D5E")

 response = client.models.generate_content(

    model="gemini-3-flash-preview",

    contents= f"""
    act as an weather assistant ,give me suggestions on clothing,skincare based on 
    the data i am providing you {data},be clear and consice.

                           """,
)
 return response.text

 print(response.text)
with st.sidebar:
    textt=st.text_input("enter city name")
    btn=st.button("submit city name")
    if btn:
        data=api_data(textt)
        #st.write(data["main"])
        col1,col2 = st.columns(2)
        with col1:
         st.metric("temp",data["main"]["temp"])
        with col2:
         st.metric("humidity",data["main"]["humidity"])

if btn:
   st.write(llm_call(api_data(textt)))
#st.write(api_data("hyderabad"))
