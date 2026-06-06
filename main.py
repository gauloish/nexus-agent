from agno.os import AgentOS

from src.agents import agent
from dotenv import load_dotenv

load_dotenv()

agent_os = AgentOS(agents=[agent()])
app = agent_os.get_app()


if __name__ == "__main__":
    agent_os.serve(
        app="main:app",
        # reload=True,
    )
