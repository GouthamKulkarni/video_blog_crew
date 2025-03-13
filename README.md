# video_blog_crew
This is a multi agent ai application to generate blog from a YouTube channel video using CrewAI
## Flow:
- Agents - An autonomous specialist and responsible in running a specific task
- tasks - Specific job or assignment
- tools - skill or function that agent utilize to accomplish a task
- crew - Group of agents aim to collectively work and finsh give task uising tool

## Create and use .env file under yt/.env to store your OpenAI/Groq API Keys
- Make sure that if yoou are using any other api key instead of openai, please add as below. I am using groq here. And keep second line as is. Otherwise it will give ann error.
  GROQ_API_KEY=<your_api_key>
  OPENAI_API_KEY=dummy_key
- If you are using OpenAI then just keep respective key.
  OPENAI_API_KEY=<your-openai-key>
## Refer my yt/env.txt file to create a venv in macos and activate. During the development if any errors appear use below pip commands. I see there are mutliple error while installing crewai and crewai tool
- pip install setuptools_rust
- export PYO3_USE_ABI3_FORWARD_COMPATIBILITY="1"

## Use yt/requirements.txt to install dependecies
- pip install -r requirements.txt

## yt/blog_post.md is the content generated from the agent.

## yt/deps.txt is just for reference of dependecies and their versions.
