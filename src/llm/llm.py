import streamlit as st
from groq import Groq

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

chatBot = Groq(api_key=GROQ_API_KEY)

with open("src/llm/instruction.txt","r") as file:
    instruction=file.read()


def get_response(question,msg_history):

  
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"system",
            "content":instruction
        }
    ]
    
    #Storing the session chats in messages 
    for msg in msg_history:
        if msg["role"] == "User":
            messages.append({
                "role": "user",
                "content": msg["content"]
            })

        elif msg["role"] == "Krishna":
            messages.append({
                "role": "assistant",
                "content": msg["content"]
            })

    
    messages.append({
        "role": "user",
        "content": question
    })

    completion = chatBot.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=2048,
        reasoning_effort="medium",
        stream=False
    )
    
    return completion.choices[0].message.content