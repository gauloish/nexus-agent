from pathlib import Path

from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.qdrant import Qdrant

from google.oauth2 import service_account

from src.knowledge.ingestion import ingest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
COLLECTION_NAME = "nexus-collection"


def agent() -> Agent:
    """Create the main agent for nexus application

    Returns:
        Agent: Nexus agent
    """

    credentials_path = PROJECT_ROOT / "credentials.json"
    files_path = PROJECT_ROOT / "resource/files_test.json"

    credentials = service_account.Credentials.from_service_account_file(
        filename=credentials_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )

    model = Gemini(
        id="gemini-2.5-flash",
        vertexai=True,
        credentials=credentials,
    )

    embedder = GeminiEmbedder(
        id="gemini-embedding-001",
        vertexai=True,
    )

    vector_db = Qdrant(
        collection=COLLECTION_NAME,
        url="http://localhost:6333",
        embedder=embedder,
    )

    knowledge = Knowledge(
        vector_db=vector_db,
    )

    ingest(knowledge, files_path)

    return Agent(
        name="Nexus Agent",
        model=model,
        knowledge=knowledge,
    )