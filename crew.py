from crewai import Crew, Process
from agents import readerAgent, summarizerAgent
from tasks import readPaperTask, summarizeTask

def literature_review_crew():
    return Crew(
        agents=[
            readerAgent(),
            summarizerAgent()
        ],
        tasks=[
            readPaperTask(),
            summarizeTask()
        ],
        verbose=True,  
        process=Process.sequential 
    )
