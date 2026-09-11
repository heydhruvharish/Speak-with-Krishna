import streamlit as st 
from src.components.wallpaper import wallpaper
from src.UI.login_page import layout
from src.database.db import register_user
import time 
from src.database.db import user_login
from src.screens.chat import chat

def home_screen():
    if st.session_state["page"]=="chat":
        chat()
    elif st.session_state["home"]=="register":
        register()
    else:
        login()
    
def register():
    wallpaper()

    layout()
    st.markdown(
    "<h1 style='text-align: center;'>Register</h1>",
    unsafe_allow_html=True,
    )
    name = st.text_input("Name",placeholder="Dhruv")
    username = st.text_input("Username",placeholder="Username")
    password = st.text_input("Password", type="password",placeholder="Password")
    
    
   
    col1,col2=st.columns(2)
    with col1:
        if st.button("Register",icon=":material/passkey:"):
            if not name or not username or not password:
                st.error("Fill all the fields")
                time.sleep(2)
                st.rerun()
            
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
    wallpaper()
    layout()
    
    st.markdown(
    "<h1 style='text-align: center;'>Login</h1>",
    unsafe_allow_html=True,
    )
    
    username = st.text_input("Username",placeholder="Username")
    password = st.text_input("Password", type="password",placeholder="Password")
    
   
    col1,col2=st.columns(2)
    with col1:
        
        if st.button("Login",icon=":material/passkey:"):
            if not username or not password:
                st.error("Fill all the fields")
                time.sleep(1)
                st.rerun()
            if check(username,password):
                st.toast("Login successful",icon="✅")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Username and/or password incorrect")
           
            
    with col2:
        if st.button("Don't have an account ? Register here",width="stretch"):
            st.session_state["home"]="register"
            st.rerun()
           

def check(username,password):
    user_data=user_login(username,password)
    
    if user_data:
        st.session_state["data"]=user_data
        st.session_state["page"]="chat"
        
        return True
    else:
        return False