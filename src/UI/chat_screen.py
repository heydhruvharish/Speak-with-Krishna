import streamlit as st


def chat_ui():

    st.markdown("""
        <style>
        /* Hide Top Bar of streamlit */    
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        .chat-title {
            font-size: 28px;
            font-weight: 700;
        }

        .chat-subtitle {
            font-size: 13px;
            opacity: 0.6;
        }

        </style>
    """, unsafe_allow_html=True)


    # Header
    col1, col2 = st.columns([8, 2])

    with col1:
        st.markdown(
            """
            <div class="chat-title">🦚 Krishna</div>
            <div class="chat-subtitle">
                Ask Krishna your questions
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if st.button("Sign Out",key="signout_button",width="stretch"):
            st.session_state["home"]="login"
            st.session_state["page"]="home"
            del st.session_state["data"]
            del st.session_state["message_history"]
            st.rerun()