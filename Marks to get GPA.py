import streamlit as st

st.title("Student Marks Grading App")

st.subheader("Enter your marks for each subject")

# Number of subjects input
num_subjects = st.number_input("Number of subjects", min_value=1, max_value=20, step=1)

marks = []
for i in range(num_subjects):
    mark = st.number_input(f"Enter mark for Subject {i+1}", min_value=0, max_value=100)
    marks.append(mark)

if st.button("Calculate Results"):
    total = sum(marks)
    average = total / num_subjects

    # Function to determine GPA and remark
    def get_gpa(m):
        if m >= 80:
            return 5.0, "Excellent"
        elif m >= 70:
            return 4.0, "Very Good"
        elif m >= 60:
            return 3.0, "Good"
        elif m >= 50:
            return 2.0, "Pass"
        elif m >= 40:
            return 1.0, "Poor"
        else:
            return 0.0, "Fail"

    gpas = []
    remarks = []

    for m in marks:
        gpa, remark = get_gpa(m)
        gpas.append(gpa)
        remarks.append(remark)

    avg_gpa = sum(gpas) / len(gpas)

    st.success(f"🔢 Average Mark: {average:.2f}")
    st.info(f"📊 Overall GPA: {avg_gpa:.2f}")

    for i, (mark, gpa, remark) in enumerate(zip(marks, gpas, remarks)):
        st.write(f"Subject {i+1}: Mark = {mark}, GPA = {gpa}, Remark = {remark}")
