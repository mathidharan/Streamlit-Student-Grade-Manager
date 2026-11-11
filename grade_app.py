
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = []


# Grade calculation
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Application title
st.title("🎓 Student Grade Manager")
st.write("Manage student marks and calculate grades.")

st.divider()

# Add student form
st.subheader("Add New Student")

with st.form("add_student_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Student Name")

    with col2:
        mark = st.number_input(
            "Student Mark",
            min_value=0,
            max_value=100,
            value=0,
            step=1
        )

    submitted = st.form_submit_button(
        "➕ Add Student",
        use_container_width=True
    )

    if submitted:
        if not name.strip():
            st.error("Please enter student name.")
        else:
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


st.divider()

# Display students
st.subheader("Student Results")

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    # Class calculations
    marks = [student["Mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{average:.2f}")
    col2.metric("Highest Mark", highest)
    col3.metric("Lowest Mark", lowest)

    st.write("### Student Details")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Clear all students
    if st.button("🗑️ Clear All Students"):
        st.session_state.students = []
        st.rerun()

else:
    st.info("No students added yet. Add your first student above.")
