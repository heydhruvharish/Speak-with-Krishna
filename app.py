import streamlit as st
from src.screens.home_screen import home_screen

def main():
    if "home" not in st.session_state:
        st.session_state["home"]="register"
    
    
    home_screen()
    
main()