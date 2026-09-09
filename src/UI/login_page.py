import streamlit as st

def layout():
    st.markdown("""
    <style>

    /* Move main content above the video */
    .stMainBlockContainer {
        position: relative;
        z-index: 10;
    }

    /* Authentication box */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(0, 0, 0, 0.85) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: 20px !important;
        padding: 30px !important;

        max-width: 450px;
        margin: 80px auto !important;

        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    }

    /* Input boxes */
    div[data-testid="stTextInput"] input {
        background-color: rgba(255, 255, 255, 0.12) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
    }

    /* Input labels */
    div[data-testid="stTextInput"] label {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)


    with st.container(border=True):

        st.markdown("""
        <h1 style="
            text-align:center;
            color:white;
            margin-bottom:5px;
        ">
            Create Account
        </h1>

        <p style="
            text-align:center;
            color:#cccccc;
            margin-bottom:25px;
        ">
            Register to continue
        </p>
        """, unsafe_allow_html=True)
