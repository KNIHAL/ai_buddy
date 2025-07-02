from crewai import Agent
from crewai_tools import VisionTool
from ai_core import Cloudllm
from tools import DocloaderTool

tools = [VisionTool(), DocloaderTool()]

def readerAgent():
    return Agent(
        role="Reader Agent",
        goal="Extract all relevant content and data from research PDFs, images, and documents with high accuracy.",
        backstory=(
            "You are an expert in reading and extracting information from academic research material, "
            "whether it's scanned documents, screenshots, or structured PDFs. "
            "You never miss important figures, formulas, or small notes in footers or headers."
        ),
        verbose=True,
        allow_delegation=False,
        llm=Cloudllm(),
        tools=tools
    )
