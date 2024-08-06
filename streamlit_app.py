import streamlit as st
import pandas as pd
import datetime
#D:\OneDrive\Desktop\Projects>streamlit run black-tiger-ma-v3.py
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
                        belts = ["4 Dan","3 Dan","2 Dan","1 Dan","Brown","Brown/White","Green","Green/White","Yellow","Yellow/White","Blue","Blue/White","Red","Red/White","White/Red","White"]
                        GradeI = int(Grade) + 3
                        GradeN = int(Grade) + 2
                        belt = belts[GradeI]
                        nbelt = belts[GradeN]
                        syllabus4db = "4 Dan: Basics - "
                        syllabus4ds = "4 Dan: Strikes - "
                        syllabus4dg = "4 Dan: Grapples - "
                        syllabus3db = "3 Dan: Basics - "
                        syllabus3ds = "3 Dan: Strikes - "
                        syllabus3dg = "3 Dan: Grapples - "
                        syllabus2db = "2 Dan: Basics - "
                        syllabus2ds = "2 Dan: Strikes - "
                        syllabus2dg = "2 Dan: Grapples - "
                        syllabus1db = "1 Dan: Basics - "
                        syllabus1ds = "1 Dan: Strikes - "
                        syllabus1dg = "1 Dan: Grapples - "
                        syllabus1b = "Brown: Basics - "
                        syllabus1s = "Brown: Strikes - "
                        syllabus1g = "Brown: Grapples - "
                        syllabus2b = "Brown/White: Basics - "
                        syllabus2s = "Brown/White: Strikes - "
                        syllabus2g = "Brown/White: Grapples - "
                        syllabus3b = "Green: Basics - "
                        syllabus3s = "Green: Strikes - "
                        syllabus3g = "Green: Grapples - "
                        syllabus4b = "Green/White: Basics - "
                        syllabus4s = "Green/White: Strikes - "
                        syllabus4g = "Green/White: Grapples - "
                        syllabus5b = "Yellow: Basics - "
                        syllabus5s = "Yellow: Strikes  - "
                        syllabus5g = "Yellow: Grapples - "
                        syllabus6b = "Yellow/White: Basics - "
                        syllabus6s = "Yellow/White: Strikes - "
                        syllabus6g = "Yellow/White: Grapples - "
                        syllabus7b = "Blue: Basics - "
                        syllabus7s = "Blue: Strikes - "
                        syllabus7g = "Blue: Grapples - "
                        syllabus8b = "Blue/White: Basics - "
                        syllabus8s = "Blue/White: Strikes - "
                        syllabus8g = "Blue/White: Grapples - "
                        syllabus9b = "Red: Basics - "
                        syllabus9s = "Red: Strikes - "
                        syllabus9g = "Red: Grapples - "
                        syllabus10b = "Red: Basics - "
                        syllabus10s = "Red: Strikes - "
                        syllabus10g = "Red: Grapples - "
                        syllabus11b = "Red/White: Basics - "
                        syllabus11s = "Red/White: Strikes - "
                        syllabus11g = "Red/White: Grapples - "
                        syllabus12b = "White/Red: Basics - "
                        syllabus12s = "White/Red: Strikes - "
                        syllabus12g = "White/Red: Grapples - " 
                        st.write("Hi " + forename + " our records indicate you are a " + belt + " belt." + " Your next belt is " + nbelt)
                        st.write(Grade)
                        if belt == "3 Dan":
                            st.write(syllabus4db)
                            st.write(syllabus4ds)
                            st.write(syllabus4dg) 
                        elif belt == "2 Dan":
                            st.write(syllabus3db)
                            st.write(syllabus3ds)
                            st.write(syllabus3dg) 
                        elif belt == "1 Dan":
                            st.write(syllabus2db)
                            st.write(syllabus2ds)
                            st.write(syllabus2dg) 
                        elif belt == "Brown":
                            st.write(syllabus1db)
                            st.write(syllabus1ds)
                            st.write(syllabus1dg)                   
                        elif belt == "Brown/White":
                            st.write(syllabus1b)
                            st.write(syllabus1s)
                            st.write(syllabus1g)
                        elif belt == "Green":
                            st.write(syllabus2b)
                            st.write(syllabus2s)
                            st.write(syllabus2g)
                        elif belt == "Green/White":
                            st.write(syllabus3b)
                            st.write(syllabus3s)
                            st.write(syllabus3g)
                        elif belt == "Yellow":
                            st.write(syllabus4b)
                            st.write(syllabus4s)
                            st.write(syllabus4g)
                        elif belt == "Yellow/White":
                            st.write(syllabus5b)
                            st.write(syllabus5s)
                            st.write(syllabus5g)
                        elif belt == "Blue":
                            st.write(syllabus6b)
                            st.write(syllabus6s)
                            st.write(syllabus6g)
                        elif belt == "Blue/White":
                            st.write(syllabus7b)
                            st.write(syllabus7s)
                            st.write(syllabus7g)
                        elif belt == "Red":
                            st.write(syllabus8b)
                            st.write(syllabus8s)
                            st.write(syllabus8g)
                        elif belt == "Red/White":
                            st.write(syllabus9b)
                            st.write(syllabus9s)
                            st.write(syllabus9g)
                        elif belt == "White/Red":
                            st.write(syllabus10b)
                            st.write(syllabus10s)
                            st.write(syllabus10g)
                        elif belt == "White":
                            st.write(syllabus11b)
                            st.write(syllabus11s)
                            st.write(syllabus11g)
                        else:
                            st.write(syllabus12b)
                            st.write(syllabus12s)
                            st.write(syllabus12g)
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
