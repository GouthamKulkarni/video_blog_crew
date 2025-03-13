from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
#from crewai import Agent, LLM
load_dotenv()
llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.environ.get("GROQ_API_KEY")
)
response = llm.invoke("Hello, world!")
print(response.content)

