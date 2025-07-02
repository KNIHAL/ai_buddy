import os
from crewai import Agent
from crewai_tools import SerperDevTool, FileWriteTool
from ai_core import Cloudllm

serper_tool = SerperDevTool(
    api_key=os.getenv("SERPER_API_KEY")
)
file_write=FileWriteTool()

def summarizerAgent():
    return Agent(
        role="Summarizer Agent",
        goal="Summarize any provided PDF, text, or research material in clean, simple, and understandable language.",
        backstory=(
            "You're an expert at turning complex academic or technical material into clear and digestible summaries. "
            "You break down large topics into smaller chunks and summarize them one by one. "
            "You ensure that your output is easy to understand even for students or beginners. "
            "Your summaries are not just accurate, but also easy to remember and reuse."
        ),
        verbose=False,
        memory=True,
        llm=Cloudllm(),
        tools=[serper_tool, file_write]
    )
