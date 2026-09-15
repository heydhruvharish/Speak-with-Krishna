#Enter environment .\venv\Scripts\Activate.ps1

import streamlit as st
from src.screens.home_screen import home_screen


def main():
    st.set_page_config(
    page_title="Speak with Madhav",
    page_icon="src/assets/krishna.png"
    )
    if "home" not in st.session_state:
        st.session_state["home"]="register"
    
    if "page" not in st.session_state:
        st.session_state["page"]="home"
    
    home_screen()
    
main()