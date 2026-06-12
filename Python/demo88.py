import streamlit as st

st.title("Harsh Jasoliya")

No1 = st.text_input("Enter No.1")
No2 = st.text_input("Enter No.2")
col1, col2, col3, col4 = st.columns(4)

if st.button("Add"):
        result = int(No1) + int(No2)
        st.success(f"Sum = {result}")
elif st.button("sub"):
        result = int(No1) - int(No2)
        st.success(f"Sub is ={result}")
elif st.button("muliply"):
        result = int(No1) * int (No2)
        st.success(f"Mul is {result}")
elif st.button("divide"):
        result = int(No1) / int (No2)
        st.success(f"Mul is {result}")
        