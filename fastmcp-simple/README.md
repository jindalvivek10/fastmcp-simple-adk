# FastMCP Simple Example

This project demonstrates a simple implementation of FastMCP with a Google ADK agent (We need to modify this.)

## Running the Server

### With a Server Manager (e.g., FastMCP VS Code Extension)

To run the MCP server using a server manager, you can use the following configuration. The server manager should be configured to use the specified directory as the working directory for the command.

```json
{
  "mcpServers": {
    "fastmcp-simple": {
      "command": "uv",
      "args": [
        "run",
        "fastmcp-simple"
      ],
      "workingDirectory": "/absolute/path/to/fastmcp-simple"
    }
  }
}
```

**Note:** The `/absolute/path/to/fastmcp-simple` should be replaced with the actual absolute path to this project's directory on your machine.

### Manually

To run the server manually from your terminal, you must first navigate to the project directory:

```sh
cd /path/to/your/fastmcp-simple
```

Then, you can run the server with the following command:

```sh
uv run fastmcp-simple
``` 
