import streamlit as st
import sqlite3

def connect_db():
    return sqlite3.connect("courses.db" , check_same_thread=False)

def get_courses(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses WHERE name = ?", (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows
 
st.title(" Course Details ")
 
name = st.text_input("Enter username")
 
if st.button("Get Details"):
    if name:
        courses = get_courses(name)
        if courses:
            st.write(f" 📚 Courses for **{name}**:")
            for i, course in enumerate(courses, 1):
                st.write(f"{i}. **{course[1]}** (Duration: {course[2]}) — Author: *{course[3]}*")
        else:
            st.write("No courses found.")
    else:
        st.write("Please enter a username.")
 