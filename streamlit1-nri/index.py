import streamlit as st
import pandas as pd

st.header("hi enter the page")
btn =st.button("submit")
if "count" not in st.session_state:
    st.session_state["count"]=0
def count1():
    st.session_state["count"]=st.session_state["count"]+1
    return st.session_state["count"]
if btn:
   
   st.write(count1())




























 # makes it bold,if we put one star it coneverts to italic we can also nake just name bold with the remaining text like iam **saisree**
#st.markdown("""
             
#import streamlit as st
#import pandas as pd
            
#te="sisree" """)
#st.markdown("[streamlit](https://www.w3schools.com/)")
#st.title("hi this is streamlit page")
#st.header("this is header 1")
#st.subheader("hi iam subheader")
#dataa= {
 #   "Name": ["Alice", "Bob", "Charlie"],
  #  "Age": [23, 25, 22],
   # "City": ["New York", "Texas", "California"]
#}

#data = pd.DataFrame(dataa)


#st.write("# hi welcome to streamlit")
#st.write({

 #   "hello":"saisree",
  #  "ram":"hi"
    
#})
#st.write(data)
#st.text("hi am sree")
#st.text("""
 #           li1
  #      li2
   #     li3
    #    li4
#
#""")
