import streamlit as st
import pandas as pd
import datetime
#D:\OneDrive\Desktop\Projects>streamlit run black-tiger-ma.py
st.image("black-tiger-ma.jpg")
def login():
    st.title("Login")
    enterusername = st.text_input("Please enter email address to update system")
    enterpassword = st.text_input("Please enter password", type="password")
    if st.button("Check User"):
        file = open("black-tiger-ma.csv", "r", encoding="utf-8-sig")
        user_found = False
        for line in file:
            lines = line.strip().split(",")

            username = lines[0]
            password = lines[1]
            if enterusername == username and enterpassword == password:
                with open("black-tiger-ma-log.csv", "a", newline='') as file:
                    file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")                
                    st.session_state.logged_in = True
                    st.success("Login Successful")
                    user_found = True
                    break
        if not user_found:
            st.error("Invalid username or password")
        file.close()

def dashboard():
    st.write("Welcome Admin")
    if st.button("Sign Out"):
        st.session_state.logged_in = False
    st.title("User Management and Login Record")
    choice = st.radio("Please select add or remove",
    [":rainbow[Add]", ":rainbow[Remove]", ":rainbow[View]"])
    if choice == ":rainbow[Add]":
        username = st.text_input("Please enter email to add user")
        password = st.text_input("Please enter password for user", type="password")
        surname = st.text_input("Please enter surname")
        forename = st.text_input("Please enter forename")
        DOB = st.date_input("Please enter date of birth", format="DD/MM/YYYY")
        grade = st.selectbox("Please current grade",
        (1,2,3,4,5,6,7,8,9,10,11,12,"1 Degree","2 Degree","3 Degree","4 Degree"))
        GradingDate = st.date_input("Please enter last grading date", format="DD/MM/YYYY")
        if st.button("Add User"):
            with open("black-tiger-ma.csv", "a", newline='') as file:
                file.write(username + "," + password + "," + surname + "," + forename + "," + str(DOB) + "," + str(grade) + "," + str(GradingDate) + "\n")
    elif choice == ":rainbow[Remove]":
        username = st.text_input("Please enter username to remove")
        if st.button("Remove User"):
            df = pd.read_csv("black-tiger-ma.csv")
            if username in df["username"].values:
                df = df[df["username"] != username]
                df.to_csv("black-tiger-ma.csv", index=False)
                st.success(f"User {username} removed successfully.")
            else:
                st.error(f"Username {username} not found in the data.")          
    else:
        df = pd.read_csv("black-tiger-ma.csv")
        st.dataframe(df)
        df = pd.read_csv("black-tiger-ma-log.csv")
        st.dataframe(df)
        
if "logged_in" not in st.session_state:
    st.session_state.logged_in=False

if st.session_state.logged_in:
    dashboard()
else:
    login()

