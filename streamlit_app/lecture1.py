import streamlit as st
st.title("hello streamlit")
st.subheader("this is a subheadder")
st.text("welcome to your first streamlit app")
st.write("welcome to your first streamlit app")

chai=st.selectbox("which chai do you like?",["masala chai","ginger chai","tulsi chai","lemon chai"])
st.write(f"you have selected : {chai} , great choice")

st.success("your order has been placed successfully")


programming_language=st.selectbox("which programming language do you like?",["python","java","c++","c","javascript","ruby"])
st.write(f"you have selected: {programming_language}, nice choice!")
st.success("you have selected you favourite language")