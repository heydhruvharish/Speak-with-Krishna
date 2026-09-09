import streamlit as st 
from src.components.wallpaper import wallpaper
from src.UI.login_page import layout
from src.database.db import register_user
import time 

def home_screen():
    wallpaper()
    if st.session_state["home"]=="register":
        register()
    else:
        login()
    
def register():
    layout()
 
    name = st.text_input("Name",placeholder="Dhruv")
    username = st.text_input("Username",placeholder="Username")
    password = st.text_input("Password", type="password",placeholder="Password")
    
   
    col1,col2=st.columns(2)
    with col1:
        if st.button("Register",icon=":material/passkey:"):
            if not name or not username or not password:
                st.error("Fill all the fields")
                return
            
            success,msg=register_user(name,username,password)
        
            if success:
                st.success(msg)
                
                time.sleep(2)
                st.session_state["home"]="login"
                st.rerun()
                
            else:
                error = st.error(msg)
                time.sleep(2)
                error.empty()
                
        

            
    with col2:
        if st.button("Already have an account ? Login instead",width="stretch"):
            st.session_state["home"]="login"
            st.rerun()

def login():
    st.header("Login")
    
    if st.button("Register"):
        st.session_state["home"]="register"
        st.rerun()