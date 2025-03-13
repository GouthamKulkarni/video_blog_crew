from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research task
research_task = Task(
    description=(
        "Identify the video on {topic}. "
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3-paragraph report based on the {topic} of video content.',
    tools=[yt_tool],
    agent=blog_researcher
)

# Writing task
writing_task = Task(
    description=(
        "Get the info from the YouTube channel on the topic {topic}."
    ),
    expected_output='A 50-word blog post on the topic {topic} based on the video content.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="blog_post.md"
)