import streamlit as st

st.title("Harsh Jasoliya")

no = st.text_input("Enter No.")
if(st.button("Click Me ")):
    if int(no) % 2 == 0:
        st.write("Ans is")
        st.success("No is Even")
        st.balloons()
    else:
        st.write("Ans is")
        st.warning("No is Odd")
    