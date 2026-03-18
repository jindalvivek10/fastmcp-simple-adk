import asyncio

from fastmcp import Client
from mcp import types as mcp_types


async def main():
    # Connect via stdio to a local script
    async with Client("fastmcp_simple/server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

        print("\n=== Calling desktop tool...")
        result = await client.call_tool("desktop")
        if result and result[0] and isinstance(result[0], mcp_types.TextContent):
            print(f"==== Result: \n{result[0].text}")

        print("\n=== Calling get_fastmcp_docs tool...")
        result = await client.call_tool(name="get_fastmcp_docs")
        if result and result[0] and isinstance(result[0], mcp_types.TextContent):
            print(f"==== Result: \n{result[0].text[:100]}")

        print("\n=== Calling greeting tool...")
        result = await client.call_tool("get_greeting", arguments={"msg": "hey how are you"})
        if result and result[0] and isinstance(result[0], mcp_types.TextContent):
            print(f"==== Result: \n{result[0].text}")        

if __name__ == "__main__":
    asyncio.run(main())
