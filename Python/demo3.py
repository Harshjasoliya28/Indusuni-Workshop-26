import streamlit as st

st.title("Harsh Jasoliya")

No1 = st.text_input("Enter No.1")
No2 = st.text_input("Enter No.2")

import streamlit as st

st.title("Harsh Jasoliya")

No1 = st.text_input("Enter No.1")
No2 = st.text_input("Enter No.2")

if(st.button("Add")):
     result = int(No1) + int(No2)
st.success(f"Sum = {result}")
st.write(result)