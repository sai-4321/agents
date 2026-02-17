import streamlit as st
import pandas as py

if "list" not in st.session_state:
    st.session_state["list"]=[]
with st.form("my form"):

 username=st.text_input("username")
 password=st.text_input("password",type="password")
 gender=st.radio("gender",["male","female","others"])
 age=st.slider("age",0,100,step=1)
 form_button=st.form_submit_button("register")
#btn=st.button("register")

#if btn:
 if form_button:
    data={
        "username":username,
        "password":password,
"gender":gender,
"age":age
    }
     
st.session_state["list"].append(data)
st.dataframe( st.session_state["list"])
print("h")
#st.text_input("username")
#st.text_input("password",type="password")
#age=st.radio("age",[10,20,30])

#text=st.text_area(
 #   label="tell about yourself",
 #   value="hello"
#)
#st.button("submit")
#btn=st.button("submit")
#st.write(btn)
