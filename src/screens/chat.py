import streamlit as st 
from src.llm.llm import get_response
from src.UI.chat_screen import chat_ui
from src.RAG.rag import rag_retriever
    
def chat():
    chat_ui()
    user_data=st.session_state["data"]
    if "message_history" not in st.session_state:
        st.header(f"Welcome {user_data["name"]}")
        st.session_state["message_history"]=[]
        
    #LOading the conversation history
    for msg in st.session_state["message_history"]:
        if msg["role"]=="User":
            with st.chat_message(msg["role"]):
                st.text(msg["content"])
        else:
            with st.chat_message(msg["role"],avatar="src/assets/krishna.png"):
                st.text(msg["content"])  


    user_input=st.chat_input("Tell me your problem")
        
    if user_input:
        #User query
        # Display user message
        st.session_state["message_history"].append({
            "role": "User",
            "content": user_input
        })

        with st.chat_message("user"):
            st.text(user_input)

        # Get Groq response
        with st.spinner("Hmmm muje sochne do.."):
            ai_message = get_response(user_input,st.session_state["message_history"],rag_retriever)

        # Store AI response
        st.session_state["message_history"].append({
            "role": "Krishna",
            "content": ai_message
        })

        # Display AI response
        with st.chat_message("assistant",avatar="src/assets/krishna.png"):
            st.text(ai_message)
            
    
            
        
    
        
    
    