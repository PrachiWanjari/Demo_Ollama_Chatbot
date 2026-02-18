from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


#creatig my project 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assisstant, please respond to question asked."),
        ("user", "Question: {question}")
    ]
)

#streamlit framework
st.title ("Langchain demo Chat App with gemma:2b")
input_text = st.text_input("What question do you have in mind ?")

#ollama llm model
llm = Ollama(model = "gemma:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))