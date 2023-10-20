import streamlit as st
import joblib
import time
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(layout="wide")
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



# to import css file into streamlit
with open('mcd.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
   
#css file for contact form 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    
d1 = pd.read_csv('heart.csv')
d2 = pd.read_csv('stroke_feature.csv')
d3 = pd.read_csv('lung_feature.csv')

heart_model = joblib.load("heart_model.pkl")
lung_model = joblib.load("lung_model.pkl")
stroke_model = joblib.load("stroke_model.pkl")



#side bar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home','Heart Disease Prediction',
                            'Lung Disease Prediction',
                            'Stroke Disease Prediction',
                            'Contact Us'],
                           icons = ['house','heart-pulse-fill','lungs','activity', 'envelope'],
                           default_index = 0,
    )


                            
#login/signup page

# if selected == 'Login / SignUp':
#     #connect base
#     from deta import Deta
#     import datetime
#     import re
#     DETA_KEY = 'a0hmzjsaglk_Nv2e9at6DnRkgcpPSQa7RTthC1aLjGtc'
#     deta = Deta(DETA_KEY)
#     db = deta.Base('disease_prediction')
    
#     #insert user into database
#     def insert_user(email, username, password):
#         date_joined = str(datetime.datetime.now())
#         return db.put({'key':email, 'username':username, 'password':password, 'date_joined':date_joined})
    
    
#     #fetch users from database
#     def fetch_users():
#         users = db.fetch()
#         return users.items
    
#     #returns list of emails in db
#     def get_user_emails():
#         users = db.fetch()
#         emails = []
#         for user in users.items:
#             emails.append(user['key'])
#         return emails
    
#     #return list of usernames in db
#     def get_usernames():
#         users = db.fetch()
#         usernames = []
#         for user in users.items:
#             usernames.append(user['key'])
#         return usernames
    
    
#     #validate the email
#     def validate_email(email):
#         pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        
#         if re.match(pattern, email):
#             return True
#         return False
    
#     #validate username
#     def validate_username(username):
#         pattern = "^[a-zA-Z0-9]*$"
#         if re.match(pattern, username):
#             return True
#         return False
    
    
#     #sign up
#     signup = st.toggle('Login / SignUp')
#     def sign_up():
#         with st.form(key='my_form', clear_on_submit=True):
#             st.subheader(':orange[Sign Up]')
#             email = st.text_input('Email', placeholder='Enter your email')
#             username = st.text_input('Username', placeholder='Enter username')
#             password1 = st.text_input('Password', placeholder='Enter password', type='password')
#             password2 = st.text_input('Confirm Password', placeholder='Enter password', type='password')

#             #validation
#             if email:
#                 if validate_email(email):
#                     if email not in get_user_emails():
#                         if validate_username(username):
#                             if username not in get_usernames():
#                                 if len(username) >= 3:
#                                     if len(password1) >= 6:
#                                         if password1 == password2:
#                                             #add user to db
#                                             hashed_password = stauth.Hasher([password2]).generate()
#                                             insert_user(email, username, hashed_password[0])
#                                             st.info('Account created sucessfully', icon="✓")
#                                             time.sleep(0.5)
#                                             st.balloons()
#                                         else:
#                                             st.warning('Passwords Do not Match')
#                                     else:
#                                         st.warning('Password is too short')
#                                 else:
#                                     st.warning('Username Too short')
#                             else:
#                                 st.warning('Username Already Exists')
#                         else:
#                             st.warning('Invalid username')
#                     else:
#                         st.warning('Email aleady exists!!!')            
#                 else:
#                     st.warning('Invalid email')          
                
            
#             col0, col1,col2= st.columns(3)
#             with col0:
#                 st.form_submit_button('Sign Up')
#             with col2:
#                st.form_submit_button('Already have an account? Login')
#             #    if col2.form_submit_button("Already have an account? Login"):
#             #        st.write("Welcome")
#             #    if st.session_state.login_button_clicked:
#             #         st.write("Welcome to the login page")
#     if signup:
#         sign_up()
#     else:
#         def sign_in():
#             with st.form(key='my_form', clear_on_submit=True):
#                 st.subheader(':orange[Login]')
#                 login_user = st.text_input('Username', placeholder='Enter your username')
#                 login_password = st.text_input('Password', placeholder='Enter password', type='password')
                
#                 # Fetch the user's data based on the entered username
#                 user_data = db.get(login_user)
                
#                 if user_data:
#                     db_hashed_password = user_data['password']  # Assuming 'password' is the key for the hashed password in your database
                    
#                     if db_hashed_password == login_password:
#                         st.success('Login successful')
#                     else:
#                         st.warning('Wrong username or password')
#                 else:
#                     st.warning('Wrong username or password')

#                 col0, col1, col2 = st.columns(3)
#                 with col0:
#                     st.form_submit_button('Login')
#         sign_in()






#Home Page
if(selected == 'Home'):
    #connect base
    from deta import Deta
    import datetime
    import re
    DETA_KEY = 'a0hmzjsaglk_Nv2e9at6DnRkgcpPSQa7RTthC1aLjGtc'
    deta = Deta(DETA_KEY)
    db = deta.Base('disease_prediction')

    # Define a function to validate the user's credentials
    def validate_credentials(username, password):
        user = db.get(username)
        if user and user.get('password') == password:
            return True
        return False

    # Create a SessionState object
    class SessionState:
        def __init__(self):
            self.username = ""
            self.logged_in = False

    st.title("Sign In")

    # Create the sign-in form
    with st.form("Sign In Form"):
        chose = st.selectbox("Select an option to log in or sign up", ["Login","Signup"])
        if chose == "Login":
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            submitted = st.form_submit_button("Sign In")

    # Create a SessionState object to manage session data
    session_state = SessionState()

    # Check if the user has logged in
    if submitted and validate_credentials(username, password):
        session_state.username = username
        session_state.logged_in = True

    if session_state.logged_in:
        st.title("Welcome, " + session_state.username)
        # You can now display other pages or sections of your application here
    else:
        st.error("Invalid username or password")

# Add other sections or pages of your application below

    add_bg_from_local('1jiaxutc.png')

    # Define CSS styles for the homepage
    st.markdown(
        """
        <style>
            .header {
                font-weight: bold;
                font-family: 'Times New Roman', Times, serif;
                color: black;
                font-size: 45px;
                text-align: center;
                margin-top: 20px;
            }
            .title {
                font-weight: bold;
                font-family: 'Times New Roman', Times, serif;
                color: red;
                font-size: 36px;
                margin-top: 20px;
            }
            .section {
                padding: 20px;
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 10px;
                color: white;
            }
            .btn {
                background-color: #008CBA;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                cursor: pointer;
            }
            .btn:hover {
                background-color: orange;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the background image and header
    st.markdown('<h1 class="header">Welcome to Our Chronic Disease Prediction</h1>', unsafe_allow_html=True)

    st.markdown("<h2>Project Background</h2>", unsafe_allow_html=True)
    # Introduction section
    st.markdown('<p style = "color:black;">Chronic diseases represent a growing global health challenge that demands innovative solutions. These long-term health conditions, such as heart disease, diabetes, cancer, and respiratory disorders, have become leading causes of morbidity and mortality worldwide. The burden of chronic diseases not only affects individuals and their families but also places significant strain on healthcare systems and economies</p>', unsafe_allow_html=True)
    
    st.markdown("<h2>About Us</h2>", unsafe_allow_html=True)
    st.write("We are dedicated to providing valuable insights into chronic disease prediction.")
    st.write("Welcome to our Chronic Disease Prediction project. We are passionate about improving healthcare "
          "through data-driven insights and early disease detection. Our mission is to empower individuals "
          "to take control of their health by providing accurate and accessible disease prediction tools.")

    st.write("Key features of our project:")
    st.markdown(":red[1. **Accurate Predictions: We use advanced machine learning models to provide accurate predictions**.]", unsafe_allow_html=True)
    st.markdown(":red[2. **Early Detection: Detect chronic diseases at an early stage, increasing treatment success rates.**]")
    st.markdown(":red[3. **User-Friendly: Our user-friendly interface makes it easy for you to predict your risk.**]")
    st.markdown(":red[4. **Educational Content: We offer valuable information and resources related to each chronic disease.**]")

    st.write("Join us in the journey towards better health. Let's work together to prevent and manage chronic diseases.")
    st.markdown('<button class="btn">Let\'s begin your journey to better health!</button>', unsafe_allow_html=True)


    
#Heart Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    #set background image
    add_bg_from_local('pngwing.com (5).png')
    
    #set background color
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: darkred;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    #title page
    st.markdown('<h2 style= "color: black;"><em>Heart Disease Prediction using ML</em></h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', value=0)
    
    with col2:
        sex = st.selectbox('Sex',['','Male','Female'])
        
    with col3:
        cp = st.selectbox('Chest Pain',['','Typical Angina','Atypical Angina','Non-Angina','Asymptomatic'])
        
    with col1:
        resting_bp = st.number_input('Resting Blood Pressure', value=0)
        
    with col2:
        cholesterol = st.number_input("Cholesterol", value=0)
        
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar",['','above 120 mg/dL', 'below 120 mg/dL'])
        
    with col1:
        rest_ecg = st.number_input("Resting Electrocardiographic", value=0)
        
    with col2:
        maxheartrate = st.number_input("Max Heart Rate", value=0)
        
    with col3:
        angina = st.selectbox("Exercise Induced Angina ",['','Yes','No'])
    
    with col1:
        st_dep = st.number_input("STDepression", value=0)
        
    with col2:
        st_seg_slope = st.selectbox("ST Segment Slope",['','Upsloping','Flat','Downsloping'])
    
    with col3:
        nmj = st.number_input("Num Major Vessels(0-4)", value=0)
        
    with col1:
        tha = st.number_input("Thalassemia(0-3)", value=0)
    submitted = st.button("Submit")
        
    #code for Prediction
    if ((age is not None) and (sex is not None) and cp and (resting_bp is not None) and (cholesterol is not None) and fbs and rest_ecg and (maxheartrate is not None) and angina and (st_dep is not None) and st_seg_slope and nmj and tha):
                if submitted:
                    with st.status("Loading...."):
                        time.sleep(2)
                        st.success("Sucessful")
                    tab1, tab2 = st.tabs(["Interpretation", "Result"])
                    
                    with tab1:
                        time.sleep(3)
                    st.write("Your Inputted Data:")
                    input_var = pd.DataFrame([{'Age' : age,'Gender' : sex,'Chest Pain Type' : cp,'RestingBP' : resting_bp, 'Cholestrol' : cholesterol, 'Fastin Blood Sugar' : fbs, 'RestECG':rest_ecg, 'MaxHeartRate':maxheartrate, 'Exercise Induced Angina':angina, 'STDepression':st_dep,'STSegmentSlope':st_seg_slope, 'NumMajorVessels':nmj, 'Thalassemia': tha}])
                    st.table(input_var)
                    
                    from sklearn.preprocessing import LabelEncoder, StandardScaler
                    lb = LabelEncoder()
                    scaler = StandardScaler()
                    for i in input_var:
                        if input_var[i].dtypes == 'int' or input_var[i].dtypes == 'float':
                            input_var[[i]] = scaler.fit_transform(input_var[[i]])
                        else:
                            input_var[i] = lb.fit_transform(input_var[i])
                        
                    with tab2:
                        st.write("Your Result")
                        heart_prediction = heart_model.predict(input_var)
                        if heart_prediction == 0:
                            st.balloons('You do not have any Sign of Heart Disease')
                        else:
                            st.error('You have signs of heart disease, Please Seek Medical Help Immediately')

    
#Lung Prediction Page
if (selected == 'Lung Disease Prediction'):
    
    #background image
    add_bg_from_local('lung2.png')
    
    #title page
    st.markdown('<h2>Lung Disease Prediction using ML</h2>', unsafe_allow_html=True)
    
    #variables
    # Create the form
    with st.form("Form2", clear_on_submit=True):
        Obesity = st.slider("Obesity", 1, 7, key="Obesity")
        Cob = st.slider("Coughing of Blood", 1, 9, key="Cob")
        Ps = st.slider("Passive Smoker", 1, 8, key="Ps")
        Au = st.slider("Alcohol use", 1, 8, key="Au")
        Da = st.slider("Dust Allergy", 1, 8, key="Da")
        Gr = st.slider("Genetic Risk", 1, 7, key="Gr")

        submits = st.form_submit_button("Submit")

            
            
    if (Obesity and Cob and Ps and Au and Da and Gr):
        if submits:
            with st.status("Loading...."):
                time.sleep(2)
                st.success("Sucessful")
            tab5, tab6 = st.tabs(["Interpretation", "Result"])
                    
            with tab5:
                time.sleep(3)
            st.write(f",Your Inputted Data:")
            input_lung = pd.DataFrame([{'Obesity' : Obesity,'Coughing of Blood' : Cob,'Passive Smoker' : Ps, 'Alcohol use' : Au, 'Dust Allergy' : Da, 'Genetic Risk': Gr}])
            st.table(input_lung)
                    
            from sklearn.preprocessing import LabelEncoder, StandardScaler
            lb = LabelEncoder()
            for i in input_lung:
                    input_lung[i] = lb.fit_transform(input_lung[i])
            with tab6:
                st.write("Your Result")
                lung_prediction = lung_model.predict(input_lung)
                if lung_prediction == 0:
                    st.success('You have low risk of having Lung Cancer')
                    st.balloons()
                elif lung_prediction == 1:
                    st.warning("You have a medium risk of having Lung Cancer")
                else:
                    st.snow()
                    st.error('You have high risk of having Lung Cancer, Please Seek Medical Help Immediately')

#Stroke Prediction Page
if (selected == 'Stroke Disease Prediction'):
    
    #background image
    add_bg_from_local('brain2.png')
    
    #title page
    st.markdown('<h2>Stroke Disease Prediction using ML</h2>', unsafe_allow_html=True)
    
    #var
    age2 = st.number_input("Age", value=0)
    hypertension = st.selectbox("Hypertension", ["No", "Yes"], key="hypertension")
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"], key="heart_disease")
    bmi = st.number_input("BMI", key="bmi", value=0)
    avg_glucose_level = st.number_input("Average Glucose Level", key="avg_glucose_level", value=0)
    
    if st.button('Stroke Test Result',):
        with st.status("Loading...."):
            time.sleep(2)
            st.success("Sucessful")
        tab3, tab4 = st.tabs(["Interpretation", "Result"])
                    
        with tab3:
            time.sleep(3)
            st.write("Your Inputted Data:")
            input_stroke = pd.DataFrame([{'age' : age2,'hypertension' : hypertension,'heart_disease' : heart_disease, 'bmi' : bmi, 'avg_glucose_level' : avg_glucose_level}])
            st.table(input_stroke)
                    
            from sklearn.preprocessing import LabelEncoder, StandardScaler
            lb = LabelEncoder()
            scaler = StandardScaler()
            for i in input_stroke:
                if input_stroke[i].dtypes == 'int' or input_stroke[i].dtypes == 'float':
                    input_stroke[[i]] = scaler.fit_transform(input_stroke[[i]])
                else:
                    input_stroke[i] = lb.fit_transform(input_stroke[i])
            with tab4:
                st.write("Your Result")
                stroke_prediction = stroke_model.predict(input_stroke)
                if stroke_prediction == 0:
                    st.success('You do not have any sign of Stroke Disease')
                    st.balloons()
                else:
                    st.snow()
                    st.error('You may have signs of Stroke disease, Please Seek Medical Help Immediately')
    
  
  
#Contact Us Page  
if (selected == 'Contact Us'):
    
    #background image
    add_bg_from_local('contact1.png')
    
    #title page
    st.header(":mailbox: Get In Touch With Me!")

    #form
    contact_form = """
    <style>
        form {
            background-color: rgba(0, 0, 0, 0.9);
            padding: 20px;
            border-radius: 10px;
            text-align: center; /* Center align the form content */
        }
        .centered-button {
            display: block;
            margin: 0 auto; /* Center the button horizontally */
        }
    </style>
    <form action="https://formsubmit.co/elohougeh@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <input type="hidden" name="_autoresponse" value="Thank you for your message, Please hold on while our team gets in contact with you :)">
        <button class="centered-button" type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)