from langchain_core.documents import Document
from langchain_community.document_loaders import (
    CSVLoader,
    JSONLoader,
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader
)

import os
from crewai_tools import BaseTool

class DocloaderTool(BaseTool):
    name = "UniversalReadTool"
    description = "Reads text content from PDF, DOCX, TXT, CSV, and JSON files using Langchain loaders"

    def _run(self, file_path: str) -> list[Document]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        file_path = file_path.strip().lower()

        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file_path.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        elif file_path.endswith(".txt"):
            loader = TextLoader(file_path)
        elif file_path.endswith(".csv"):
            loader = CSVLoader(file_path)
        elif file_path.endswith(".json"):
            loader = JSONLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path}")

        return loader.load()
