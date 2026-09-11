import streamlit as st
from groq import Groq

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

chatBot = Groq(api_key=GROQ_API_KEY)

with open("src/llm/instruction.txt","r") as file:
    instruction=file.read()


def get_response(question):

    completion = chatBot.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": question
            },
            {
              "role":"system",
              "content":instruction
            }
        ],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False
    )

    return completion.choices[0].message.content