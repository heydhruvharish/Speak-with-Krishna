import streamlit as st
from groq import Groq
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

chatBot = Groq(api_key=GROQ_API_KEY)

with open("src/llm/instruction.txt","r") as file:
    instruction=file.read()


def get_response(question,msg_history,retriever):

    results=retriever.retrieve(question)
    # DEBUG (Checking if retrival is happening or not)
    # print("\n========== RAG DEBUG ==========")
    # print("QUESTION:", question)
    # print("DOCUMENTS RETRIEVED:", len(results))

    # for i, doc in enumerate(results):
    #     print(f"\n--- DOCUMENT {i + 1} ---")
    #     print("Similarity:", doc["similarity_score"])
    #     print("Content:", doc["document"][:500])

    
    # print("========== END RAG DEBUG ==========\n")
    
    
    context = "\n".join([doc["document"] for doc in results]) if results else ""
    rag_instruction = f""" {instruction} Relevant information retrieved from the Bhagavad Gita: --- CONTEXT --- {context} --- END CONTEXT --- Use the above context to help answer the user's question. """
    
    
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"system",
            "content":rag_instruction
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
    #Completion contains many info ID,model,choices,usage 
    #choices is a list of possible generated responses.
    #[0] Means give me the first generated response ,in this case ,n=1 therefore only 1 response is generated anyway
    return completion.choices[0].message.content