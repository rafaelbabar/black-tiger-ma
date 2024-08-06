import streamlit as st
import pandas as pd
import datetime
#D:\OneDrive\Desktop\Projects>streamlit run black-tiger-ma-v2.py
st.image("black-tiger-ma.jpg")
def login():
    selection = st.radio("Please choose Login or New User",
    [":rainbow[Login]", ":rainbow[New User]"])
    if selection == ":rainbow[Login]":
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
                surname = lines[2]
                forename = lines[3]
                Grade = lines[5]
                GradingDate = lines[6]
                admin = lines[7]
                if enterusername == username and enterpassword == password and admin == "Y":
                    with open("black-tiger-ma-log.csv", "a", newline='') as file:
                        file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")                
                        st.session_state.logged_in = True
                        st.success("Login Successful")
                        user_found = True
                        break
                if enterusername == username and enterpassword == password and admin == "N":
                    with open("black-tiger-ma-log.csv", "a", newline='') as file:
                        file.write(username + "," + str(datetime.datetime.now().replace(microsecond=0)) + "\n")                
                        user_found = True
                        belts = ["Brown","Brown/White","Green","Green/White","Yellow","Yellow/White","Blue","Blue/White","Red","Red/White","White/Red","White"]
                        GradeI = int(Grade) - 1
                        GradeN = int(Grade) - 2
                        belt = belts[GradeI]
                        nbelt = belts[GradeN]
                        st.write("Hi " + forename + " our records indicate you are a " + belt + " belt.  Your next belt is " + nbelt)
                        break              
            if not user_found:
                st.error("Invalid username or password")
            file.close()
    else:
        st.title("New User")
        username = st.text_input("Please enter email to add user")
        password = st.text_input("Please enter password for user", type="password")
        surname = st.text_input("Please enter surname")
        forename = st.text_input("Please enter forename")
        DOB = st.date_input("Please enter date of birth", format="DD/MM/YYYY")
        grade = st.selectbox("Please current grade",
        (1,2,3,4,5,6,7,8,9,10,11,12,"1 Dan","2 Dan","3 Dan","4 Dan"))
        GradingDate = st.date_input("Please enter last grading date", format="DD/MM/YYYY")
        if st.button("Add User"):
            with open("black-tiger-ma.csv", "a", newline='') as file:
                file.write(username + "," + password + "," + surname + "," + forename + "," + str(DOB) + "," + str(grade) + "," + str(GradingDate) + "," + "N" + "\n")        
def dashboard():
    st.write("Welcome Admin")
    if st.button("Sign Out"):
        st.session_state.logged_in = False
    st.title("User Management and Login Record")
    choice = st.radio("Please select add or remove",
    [":rainbow[Add]", ":rainbow[Remove]",  ":rainbow[Promote]",":rainbow[View]"])
    if choice == ":rainbow[Add]":
        username = st.text_input("Please enter email to add user")
        password = st.text_input("Please enter password for user", type="password")
        surname = st.text_input("Please enter surname")
        forename = st.text_input("Please enter forename")
        DOB = st.date_input("Please enter date of birth", format="DD/MM/YYYY")
        grade = st.selectbox("Please current grade",
        (1,2,3,4,5,6,7,8,9,10,11,12,"1 Dan","2 Dan","3 Dan","4 Dan"))
        GradingDate = st.date_input("Please enter last grading date", format="DD/MM/YYYY")
        if st.button("Add User"):
            with open("black-tiger-ma.csv", "a", newline='') as file:
                file.write(username + "," + password + "," + surname + "," + forename + "," + str(DOB) + "," + str(grade) + "," + str(GradingDate) + "," + "N" + "\n")
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
    elif choice == ":rainbow[Promote]":
        username = st.text_input("Please enter username to promote")
        df = pd.read_csv("black-tiger-ma.csv")
        if username in df["username"].values:
            grade = st.selectbox("Please select the current grade",
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "1 Dan", "2 Dan", "3 Dan", "4 Dan"))
            GradingDate = st.date_input("Please enter the last grading date", format="DD/MM/YYYY")
            if st.button("Promote User"):
                # Update the user's grade and grading date
                df.loc[df["username"] == username, "Grade"] = grade
                df.loc[df["username"] == username, "GradingDate"] = GradingDate         
                # Save the updated DataFrame back to the CSV file
                df.to_csv("black-tiger-ma.csv", index=False)         
                st.success(f"User {username} has been promoted to {grade} with grading date {GradingDate}")
        else:
            st.error("Username not found")
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
