
import os
from pathlib import Path

from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

# IMPORTANT: Dynamically compute the absolute path to your server.py script
PATH_TO_MCP_SERVER_SCRIPT = str((Path(__file__).parent.parent / "server.py").resolve())

print(PATH_TO_MCP_SERVER_SCRIPT)

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "TRUE"
os.environ["GOOGLE_CLOUD_PROJECT"] = os.environ.get("GOOGLE_CLOUD_PROJECT", "vjindal-project-ai-basic")
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"

model_config = Gemini(model="gemini-2.5-flash")


root_agent = Agent(
    name="mcp_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model = model_config,
    description="FastMCP enabled agent",
    instruction="""
     You are a highly proactive and efficient assistant
    """,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",
                args=[PATH_TO_MCP_SERVER_SCRIPT],
            )
        )
    ],
)


if __name__ == "__main__":
    import asyncio

    async def main():
        print("=== Asking the agent to use the desktop tool ===")
        response = await root_agent.run()
        print(f"\n=== Agent Response ===\n{response}")

    asyncio.run(main())
    # from google.adk.runtime import Runtime
    # runtime = Runtime(agents=[root_agent])
