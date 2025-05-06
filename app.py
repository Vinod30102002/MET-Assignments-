# A registration page
# username, password, confirm password
# terms agreement
# register button
# if pass == confirm password, the show toast as "registration successful"
# If not, show registration failed
 
import streamlit as st
st.header("Registration")


username = st.text_input("Enter username" ,placeholder="Your username")
password = st.text_input("Enter password", placeholder="Your password")
confirm_password = st.text_input("Enter your password", placeholder="password")
is_checked = st.checkbox("Agree to Terms and Conditons")

is_clicked = st.button("Login", type="primary" , use_container_width=True)
if password == confirm_password:
    st.toast("REGISTRATION SUCESSFULL")
else:
    st.toast("REGISTRATION UNSUCCESSFULL")
    