import json

from agno.knowledge.reader.pdf_reader import PDFReader
from agno.knowledge.chunking.document import DocumentChunking

def extract_files(files_path):
    """Extract from JSON content with files metadata to list of dictionary

    Args:
        files_path (str): Path to JSON file

    Returns:
        list: List of dictionary with files metadata (title and url)
    """
    data = []

    with open(files_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    return data


def ingest(knowledge, files_path):
    """Ingestion step of knowledge agent. The process consists in download, parsing and chunking
    of the files with metadata (title and url) extract from `files_path`.

    Args:
        knowledge (Knoledge): Agent knowledge
        files_path (str): Path of JSON file with metadata of the files
    """
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