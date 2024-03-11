import streamlit as st

# Define custom CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load custom CSS file
local_css("style.css")

def main():
    st.title("Student Data Display")

    # Example student data
    students = [
        {"name": "John Doe", "student_id": "001", "dob": "2000-01-01"},
        {"name": "Jane Smith", "student_id": "002", "dob": "1999-05-15"},
        {"name": "Alice Johnson", "student_id": "003", "dob": "2001-09-30"}
    ]

    # Display student data in cards
    for student in students:
        st.markdown('<div class="student-card">', unsafe_allow_html=True)
        st.write(f"**Name:** {student['name']}")
        st.write(f"**Student ID:** {student['student_id']}", f"**Date of Birth:** {student['dob']}")
        st.write(f"**Date of Birth:** {student['dob']}")
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
