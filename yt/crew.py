import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writing_task
from langchain_groq import ChatGroq
from crewai import Agent, LLM

# Load environment variables
load_dotenv()

# Ensure GROQ_API_KEY is present
if not os.environ.get("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in .env file.")

# Set a dummy OPENAI_API_KEY to bypass any lingering CrewAI dependency
os.environ["OPENAI_API_KEY"] = "dummy_key"

# Re-initialize Groq LLM (consistent with test_groq.py)
llm = LLM(
    #model="groq/llama3-8b-8192",
    model="groq/gemma2-9b-it",
    temperature=0.7
    #groq_api_key=os.environ.get("GROQ_API_KEY")
)

# Create Crew with Groq enforced
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=10,
    share_crew=True,
    manager_llm=llm,  # Enforce Groq for manager-level logic
    verbose=True  # Increase verbosity to debug LLM calls
)

# Run the crew with inputs
if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "AI VS ML VS DL VS Data Science"})
    print("Result:")
    print(result)