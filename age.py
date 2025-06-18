import streamlit as st

# Ask the user for their age
age = st.number_input("Please enter your age", min_value=0, max_value=120, step=1)

# Display the age entered by the user
if age:
    st.write(f"Your age is {age}.")
