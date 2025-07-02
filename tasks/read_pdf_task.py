from crewai import Task
from review_agent import readerAgent

def readPaperTask():
    return Task(
        description=(
            "Read the provided academic PDF, DOCX, TXT, or image and extract all relevant text content. "
            "Make sure to include any figures, equations, footnotes, and bullet points if available. "
            "The extracted text should be clean and organized for summarization."
        ),
        agent=readerAgent(),
        expected_output="Raw extracted text content from the paper, organized clearly.",
        output_file="paper_content.txt" 
    )
