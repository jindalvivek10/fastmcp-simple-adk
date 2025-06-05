import asyncio

from fastmcp import Client
from mcp import types as mcp_types


async def main():
    # Connect via stdio to a local script
    async with Client("fastmcp_simple/server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        print("\nCalling desktop tool...")
        result = await client.call_tool("desktop")
        if result and result[0] and isinstance(result[0], mcp_types.TextContent):
            print(f"Result: \n{result[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
