import streamlit as st
import pandas as pd

st.title("📘 GPA & Grading System for Multiple Students")
st.write("Upload an Excel file with students and their subject marks.")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

# GPA and Remark function
def get_gpa(mark):
    if mark >= 80:
        return 5.0, "Excellent"
    elif mark >= 70:
        return 4.0, "Very Good"
    elif mark >= 60:
        return 3.0, "Good"
    elif mark >= 50:
        return 2.0, "Pass"
    elif mark >= 40:
        return 1.0, "Poor"
    else:
        return 0.0, "Fail"

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Check if 'Name' column exists
    if 'Name' not in df.columns:
        st.error("The Excel file must include a 'Name' column for student names.")
    else:
        results = []

        for index, row in df.iterrows():
            name = row['Name']
            subjects = row.drop('Name')
            marks = subjects.values

            gpas = []
            remarks = []

            for mark in marks:
                gpa, remark = get_gpa(mark)
                gpas.append(gpa)
                remarks.append(remark)

            avg_mark = sum(marks) / len(marks)
            avg_gpa = sum(gpas) / len(gpas)

            results.append({
                "Name": name,
                "Average Mark": round(avg_mark, 2),
                "GPA": round(avg_gpa, 2),
            })

            st.subheader(f"📄 Results for: {name}")
            st.write(f"✅ Average Mark: {avg_mark:.2f}")
            st.write(f"📊 GPA: {avg_gpa:.2f}")
            for subject, mark, gpa, remark in zip(subjects.index, marks, gpas, remarks):
                st.write(f"- {subject}: {mark} → GPA: {gpa}, Remark: {remark}")
            st.markdown("---")

        # Show summary table
        st.subheader("📋 Summary Table")
        st.dataframe(pd.DataFrame(results))
