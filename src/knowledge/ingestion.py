import json

from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.document import DocumentChunking

def extract_files(files_path):
    data = []

    with open(files_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        print(data)
    
    return data


def ingest(knowledge, files_path):
    files = extract_files(files_path)

    reader = PDFReader(
        name="Document Chunking Reader",
        chunking_strategy=DocumentChunking(
            chunk_size=500,
            overlap=100,
        ),
    )

    for file in files:
        knowledge.insert(
            url=file["url"],
            metadata={"title": file["title"]},
            reader=reader,
        )