import streamlit as st

# Title of the app
st.title("Student Grading App")

# Input for student's marks
marks = st.number_input("Enter student's marks:", min_value=0, max_value=100)

# Button to evaluate the result
if st.button("Check Result"):
    if marks >= 80:
        st.success("Result: Excellent ")
    elif marks >= 50:
        st.info("Result: Good ")
    else:
        st.error("Result: Fail ")
