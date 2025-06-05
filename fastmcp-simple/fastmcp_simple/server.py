"""
FastMCP Desktop Example

A simple example that exposes the desktop directory as a resource.
"""

from pathlib import Path

import requests
from fastmcp import FastMCP

# Create server
mcp = FastMCP("Simple FastMCP Server")


@mcp.tool()
def desktop() -> list[str]:
    """List the files in the user's desktop"""
    desktop = Path.home() / "Desktop"
    return [str(f) for f in desktop.iterdir()]


# Add a dynamic greeting resource
@mcp.tool()
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.tool()
def get_fastmcp_docs() -> str:
    """Get the contents of the FastMCP docs"""
    response = requests.get("https://gofastmcp.com/llms-full.txt")
    response.raise_for_status()
    return response.text


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


def main():
    mcp.run()  # Defaults to STDIO
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=8000, path="/mcp")
    # mcp.run(transport="sse", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
