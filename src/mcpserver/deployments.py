from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers. a and b and return the result."""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers. a and b and return the result."""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers. a and b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
