from crewai import Agent, LLM
from crewai_tools import VisionTool
from tools import DocloaderTool
tools = [VisionTool(), DocloaderTool()]

cloudllm = LLM(
     model=os.getenv("GROQ_MODEL_NAME"),
     api_key=os.getenv("GROQ_API_KEY")
 )

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
        llm=cloudllm,
        tools=tools
    )
