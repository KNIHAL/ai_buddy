# 🧠 Literature Review Agent

A smart multi-agent system that reads research papers (PDF, DOCX, TXT, images), extracts content, and generates clean, student-friendly notes — powered by [CrewAI](https://crewai.com/) and LangChain tools.

---

## 🚀 What It Does

This AI agent helps students, researchers, and professionals by:

✅ Reading academic papers (PDF, DOCX, TXT, CSV, JSON, Images)  
✅ Extracting structured content from documents and screenshots  
✅ Summarizing complex ideas in simple, understandable language  
✅ Highlighting key findings and research gaps  
✅ Saving clean `.txt` summaries as notes or reports  

---

## 🧩 Architecture

Built using **CrewAI**'s multi-agent system with the following agents and tasks:

| Agent            | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| 📖 Reader Agent   | Extracts text from files and images using LangChain loaders + VisionTool |
| ✍️ Summarizer Agent | Breaks down and rewrites content into simple, student-level summaries |

---

## 🔧 Tools Used

| Tool                         | Purpose                                 |
|------------------------------|-----------------------------------------|
| `DocloaderTool`              | Reads PDFs, DOCX, TXT, etc.             |
| `FileWriteTool`              | Saves final notes in plain `.txt`       |
| `VisionTool`                 | Reads images/screenshots                |
| `SerperDevTool`              | Pulls live web data                     |

---

## 🗂️ File Structure

literature-review-agent/
├── agents/
│ ├── review_agent.py
│ └── summarizer_agent.py
├── tasks/
│ ├── read_paper_task.py
│ └── summarize_task.py
├── tools/
│ └── docloader_tool.py
├── docs/ # Stores user-uploaded input files
├── report.txt # Final generated output
├── crew.py # Sets up the CrewAI agents + tasks
├── main.py # Runs the full agent workflow
├── requirements.txt
└── README.md


---

## 🛠️ Installation

```bash
git clone https://github.com/KNIHAL/literature-review-agent.git
cd literature-review-agent
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Add env
SERPER_API_KEY=your key.
GROQ_API_KEY=your key.
GROQ_MODEL=your groq model.

### ▶️ How to Run
```bash
python main.py
```
Input your research paper path (PDF, DOCX, TXT, etc.).

Ask what you want to know about the paper.

Output will be saved in report.txt.

### 📌 Example Output Format

📚 Paper Title: Understanding Transformers in NLP
🧠 Authors: Vaswani et al.

🔍 Abstract Summary:
[Simple explanation]

🛠️ Methodology:
[Step-by-step method]

📊 Key Findings:
- Point 1
- Point 2

❓ Research Gaps:
- Missing benchmark comparisons

🧠 TL;DR:
Transformers revolutionized NLP by replacing RNNs with attention-based architectures.

### 🧠 Ideal For
Students preparing for exams or presentations.

Researchers doing literature reviews.

Educators building learning material.

Anyone who wants to understand a paper — faster!

### 🔥 Author
Built with 💻 + 🧠 by Kumar Nihal
DM me if you’re building with CrewAI!