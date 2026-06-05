from pathlib import Path

from agno.agent import Agent
from agno.models.google import Gemini

from google.oauth2 import service_account

PROJECT_ROOT = Path(__file__).resolve().parents[2]
credentials_path = PROJECT_ROOT / "credentials.json"

credentials = service_account.Credentials.from_service_account_file(
    filename=credentials_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)


def agent() -> Agent:
    """Create the main agent for nexus application

    Returns:
        Agent: Nexus agent
    """

    model = Gemini(
        id="gemini-2.5-flash",
        vertexai=True,
        project_id="infraestrutura-enap",
        location="us-central1",
        credentials=credentials,
    )

    return Agent(
        name="Nexus Agent",
        model=model,
    )