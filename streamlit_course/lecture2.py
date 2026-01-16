import streamlit as st

st.title("chai makker app")
if st.button("make chai"):
    st.success("your chai is being prepared!")


add_masalas=st.checkbox("add masalas")
if add_masalas:
    st.write("masalas added to you chai")

tea_type=st.radio("select the type of tea",["black tea","green tea","herbal tea"])

st.write(f" you have selected: {tea_type} ")

flavours=st.selectbox("select your favourite flavours",["ginger","tulsi","lemon","cardamom","cinnamon"])
st.write(f"you have selected: {flavours} flavour")

sugar_level=st.slider("select sugar level",0,10,5)
st.write(f"sugar level set to: {sugar_level}")

st.number_input("enter the number of cups",min_value=1,max_value=10,value=1,step=1)
st.write("number of cups added to your order")

name=st.text_input("enter your name")
if name:
    st.write(f"thank you {name}, your order is being processed!")

dob_today=st.date_input("enter your date of birth")
st.write(f"your date of birth is: {dob_today}")


#Assignment: Create a calculater that input date of birth and current date and output age in years, months and days
from datetime import date
dob=st.date_input(
    "Enter your date of birth:", 
    min_value=date(1900, 1, 1),  # earliest selectable date
    max_value=date.today()       # latest selectable date = today
)


# Button to calculate age
if st.button("Calculate Age"):
    today = date.today()
    
    # Calculate years, months, days
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # Adjust if days or months are negative
    if days < 0:
        months -= 1
        days += 30  # Approximate
    if months < 0:
        years -= 1
        months += 12

    # Display result
    st.success(f"You are {years} years, {months} months, and {days} days old!")