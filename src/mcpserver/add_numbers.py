from mcp.server.fastmcp import FastMCP

addmcp = FastMCP("add")


@addmcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers. a and b and return the result."""
    return a + b
