import streamlit as st
import sqlite3

# Function to create SQLite database and table if they don't exist
def create_table():
    conn = sqlite3.connect("student_data.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name TEXT, 
                 student_id TEXT,
                 dob DATE)''')
    conn.commit()
    conn.close()

# Function to insert student data into the database
def insert_data(name, student_id, dob):
    conn = sqlite3.connect("student_data.db")
    c = conn.cursor()
    c.execute('''INSERT INTO students (name, student_id, dob) 
                 VALUES (?, ?, ?)''', (name, student_id, dob))
    conn.commit()
    conn.close()

# Function to fetch and display student data from the database
def view_data():
    conn = sqlite3.connect("student_data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def main():
    st.title("Student Registration App")

    # Create the table if it doesn't exist
    create_table()

    # Input fields for Name, ID, and Date of Birth
    name = st.text_input("Name:")
    student_id = st.text_input("Student ID:")
    dob = st.date_input("Date of Birth:")

    if st.button("Register"):
        if name and student_id and dob:
            # Insert data into the database
            insert_data(name, student_id, dob)
            st.success("Registration Successful!")
            st.write("Name:", name)
            st.write("Student ID:", student_id)
            st.write("Date of Birth:", dob)
        else:
            st.error("Please fill in all fields!")

    st.header("View Registered Students")
    # Button to fetch and display student data
    if st.button("View Students"):
        data = view_data()
        if data:
            st.write("### Registered Students:")
            for student in data:
                st.write("- Name:", student[1])
                st.write("  Student ID:", student[2])
                ("  Date of Birth:", student[3])
        else:
            st.write("No students registered yet.")


if __name__ == "__main__":
    main()
