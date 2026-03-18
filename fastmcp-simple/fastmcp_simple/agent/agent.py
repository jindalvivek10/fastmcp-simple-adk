from pathlib import Path

from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

# IMPORTANT: Dynamically compute the absolute path to your server.py script
PATH_TO_MCP_SERVER_SCRIPT = str((Path(__file__).parent.parent / "server.py").resolve())

print(PATH_TO_MCP_SERVER_SCRIPT)


root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.5-flash-preview-04-17",
    description="Greeting agent",
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
        response = await root_agent.run("Please use your tools to call desktop tool for Vivek.")
        print(f"\n=== Agent Response ===\n{response}")

    asyncio.run(main())
