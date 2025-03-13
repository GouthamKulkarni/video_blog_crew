import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
#from crewai import Agent
from tools import yt_tool
from crewai import Agent, LLM
# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = LLM(
    #model="groq/llama3-8b-8192",
    model="groq/gemma2-9b-it",  # Proven to work in test_groq.py
    temperature=0.7
    #groq_api_key=os.environ.get("GROQ_API_KEY")
)

# Create a senior blog content researcher agent
blog_researcher = Agent(
    role='Senior Blog Content Researcher from YouTube videos',
    goal='Get the relevant video transcription for the topic {topic} from the provided YouTube channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI, Data Science, Machine Learning, Deep Learning, Gen AI and providing suggestions."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

# Create a senior blog writer agent
blog_writer = Agent(
    role='Senior Blog Writer',
    goal='Write a blog post on the topic {topic} based on the provided video transcription',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
)