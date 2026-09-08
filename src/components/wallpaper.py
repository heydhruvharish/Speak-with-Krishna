import streamlit as st
import base64

def wallpaper():

    video_path = "src/assets/homescreen.mp4"

    with open(video_path, "rb") as f:
        video_bytes = f.read()

    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>
             #MainMenu, footer, header {{
                visibility: hidden;
            }}
        </style>
        <video autoplay muted loop playsinline
            style="
                width: 100vw;
                height: 100vh;
                object-fit: cover;
                position: fixed;
                top: 0;
                left: 0;
            ">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )