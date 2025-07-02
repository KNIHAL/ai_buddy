from crewai import Task
from summarizer_agent import summarizerAgent

def summarizeTask():
    return Task(
        description=(
            "Summarize the extracted research text in clean, simple, and understandable language. "
            "Break the summary into the following sections:\n\n"
            "- 📄 Paper Title & Authors\n"
            "- 🧠 Abstract Summary\n"
            "- 🛠️ Methodology Summary\n"
            "- 📊 Key Findings (in bullet points)\n"
            "- ❓ Research Gaps (if any)\n"
            "- 🧠 TL;DR at the end\n\n"
            "The output should be student-friendly and well-structured."
        ),
        agent=summarizerAgent(),
        expected_output="Structured and clean summary in plain text format.",
        output_file="report.txt"
    )
