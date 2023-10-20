import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import  home, about_us, heart, lungs, stroke, contact_us, log_out
import sqlite3
# from deta import Deta
# import datetime
# import re
# DETA_KEY = 'a0hmzjsaglk_Nv2e9at6DnRkgcpPSQa7RTthC1aLjGtc'
# deta = Deta(DETA_KEY)
# db = deta.Base('disease_prediction')

st.set_page_config(
    page_title = "Biocare",
    page_icon= '🏥'
)


#.........................DESIGN BEGINS ............................
#to add picture from local computer
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_local('1jiaxutc.png')

# connect to SQLite DB
conn = sqlite3.connect('streamlit.db')
c = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
"""
# user table
c.execute(create_table_query)


def authenticate_user(username, password):
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result and result[0] == password:
        return True
    return False

def login_signup():
        st.markdown("<h1 style = 'top-margin: 0rem;text-align: center; color: #7C73C0;'>Welcome to The Shield 🛡</h1>", unsafe_allow_html=True)
        # st.markdown('Welcome to :purple[The Shield] 🛡')
        # st.title("Loging or Sign Up")
        login_signup_page = st.selectbox("Select an option to log in or sign up", ["Login", "Signup"])

        if login_signup_page == "Login":
            login_username = st.text_input("Username", placeholder='Enter Your Username')
            login_password = st.text_input("Password",placeholder='Enter Your Password', type = "password")

            if st.button("Login"):
                    
                if authenticate_user(login_username, login_password):
                    st.session_state.user = login_username
                    st.success("Login successful.")
            
                else:
                    st.error("Login failed. Enter a valid username or password.")
        
        elif login_signup_page =="Signup":
            signup_username = st.text_input("Username", placeholder= 'Enter Your Username')
            signup_password = st.text_input("Password", placeholder= 'Enter Your Password', type = "password")

            if st.button("Sign Up"):
                c.execute("INSERT INTO users VALUES (?, ?)", (signup_username, signup_password))
                conn.commit()
                st.success("Account created.")

class MultiApp:

    def _init_(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title = 'Multiple Disease Prediction System',
                options = ['Home', 'About Us', 'Heart Disease Prediction', 'Lung Disease Prediction', 'Stroke Disease Prediction','Contact Us', 'Log out'],
                icons = ['house','info','heart-pulse-fill','lungs','activity', 'envelope','lock-fill'],
                menu_icon = 'shield-fill',
                default_index = 0
    )

        if app == "Home":
            home.app()
        if app == "About Us":
            about_us.app()
        if app == "Heart Disease Prediction":
            heart.app()
        if app == "Lung Disease Prediction":
            lungs.app()
        if app == "Stroke Disease Prediction":
            stroke.app()
        if app == "Contact Us":
            contact_us.app()
        if app == "Log out":
            log_out.app()

    # run()
if __name__ == '_main_':
    if 'streamlit' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user is None:
        login_signup()
    else:
        multi_app = MultiApp()
        multi_app.add_app('Home', home.app)
        multi_app.add_app('About Us', about_us.app)
        multi_app.add_app('Heart Disease Prediction', heart.app)
        multi_app.add_app('Lung Disease Prediction', lungs.app)
        multi_app.add_app('Stroke Disease Prediction', stroke.app)
        multi_app.add_app('Contact Us', contact_us.app)
        multi_app.add_app('Log out', log_out.app)
        multi_app.run()
