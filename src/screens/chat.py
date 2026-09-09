import streamlit as st 


def chat():
    user_data=st.session_state["data"]
    
    st.header(f"Welcome {user_data["name"]}")