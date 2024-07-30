import streamlit as st
import datetime
from db import create_user, authenticate_user, update_user, getname, delete_acc

try:
    st.set_page_config(
        page_title="Empathia",
    )
except Exception as e:
    print(e)

try:
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = None
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "about" not in st.session_state:
        st.session_state.about = False
except Exception as e:
    st.toast("Something Went Wrong!! - Error STX")


def switch_page(page):
    try:
        st.session_state.page = page
    except Exception as e:
        st.toast("Something Went Wrong!! - Error SWX")

def login_page():
    try:
        st.subheader("Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type='password')

        col0_1, col0_2 = st.columns([8, 2.3])

        with col0_1:
            if st.button("Login"):
                try:
                    if authenticate_user(email, password):
                        name = getname(email)
                        st.session_state.logged_in = True
                        st.session_state.username = email
                        st.session_state.name = name
                        switch_page("chatbot")
                    else:
                        st.error("Invalid Credentials!!")
                except Exception as e:
                    st.toast("Something Went Wrong!! - Error AUF")

        with col0_2:
            if st.button("Forgot Password"):
                switch_page("forgot_password")
    except Exception as e:
        st.toast("Something Went Wrong!! - Error LPX")


def signup_page():
    try:
        st.subheader("Create New Account")
        new_name = st.text_input("Name")
        new_email = st.text_input("Email")
        new_date = str(st.date_input("Date of Birth", min_value=datetime.date(1940, 1, 1)))
        new_password = st.text_input("New Password", type='password')
        confirm_new_password = st.text_input("Confirm New Password", type='password')

        if st.button("Submit"):
            if new_password != confirm_new_password:
                st.error("Password Did not matched!!!")
            status = create_user(new_name,new_email,new_date, new_password)
            if status == 0:
                st.error("Account Already Exist!!")
            elif status == 1:
                st.success("Your Accounted has been created successfully")
                st.info("Go to Login Menu to login")
            else:
                st.error("Something Went Wrong!!")
    except Exception as e:
        st.toast("Something Went Wrong!! - Error SPX")

def forgot_password_page():
    try:
        st.subheader("Forgot Password")
        status = 999

        if st.sidebar.button("Back"):
            st.session_state.page = "login"
            st.session_state.about = False
            st.rerun()

        new_email = st.text_input("Email", type='default')
        new_date = str(st.date_input("Enter Your Date of Birth", min_value=datetime.date(1940, 1, 1)))
        new_password = st.text_input("New Password", type='password')
        confirm_new_password = st.text_input("Confirm New Password", type='password')

        if st.button("Submit"):
            if new_password != confirm_new_password:
                st.error("Password Did not matched!!!")
            else:
                status = update_user(new_email,new_date, new_password)

            if status == 0:
                st.error("Account Does't Exist!!")
            elif status == 1:
                st.error("Invalid Credentials!!")
            elif status == 2:
                st.success("Your password has been reset successfully")
                st.info("Go to Login Menu to login")
            else:
                st.error("Invalid Status!!")
    except Exception as e:
        st.toast("Something Went Wrong!! - Error FPX")

def delete_account():
    try:
        st.subheader("Delete Account")
        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password", type='password')
        if st.button("Delete Account"):
            status = delete_acc(email, password)
            if status == 0:
                st.error("Invalid Credentials!!")
            elif status == 1:
                    st.success("Account Deleted Successfully!!")
    except Exception as e:
        st.toast("Something Went Wrong!! - Error DAC")  

def show_about():
    try:
        if st.sidebar.button("Back"):
            st.session_state.page = "login"
            st.session_state.about = False
            st.rerun()
        with open("README.md", "r") as file:
            about_content = file.read()
        st.markdown(about_content, unsafe_allow_html=True)
    except Exception as e:
        st.toast("Something Went Wrong!! - Error SHB")    

def main():
    try:
        st.title("Empathia")

        if st.session_state.about:
            show_about()
        elif st.session_state.page == "chatbot":
            import chatbot
            chatbot.chatbot_interface()
        elif st.session_state.page == "forgot_password":
            forgot_password_page()
        else:
            menu = ["Login", "Sign Up", "Delete Account"]
            choice = st.sidebar.radio("Menu", menu)
            
            if st.sidebar.button("About"):
                st.session_state.about = True

            if choice == "Login":
                login_page()
            elif choice == "Sign Up":
                signup_page()
            elif choice == "Delete Account":
                delete_account()
    except Exception as e:
        st.toast("Something Went Wrong!! - Error MFX")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        st.toast("Something Went Wrong!! - Error MAF")
