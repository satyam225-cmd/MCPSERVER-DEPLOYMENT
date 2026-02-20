from loguru import logger
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers. a and b and return the result."""
    logger.debug(f"Subtracting {b} from {a}")
    result = a - b
    logger.debug(f"Subtraction result: {result}")
    return result


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers. a and b and return the result."""
    logger.debug(f"Multiplying {a} and {b}")
    result = a * b
    logger.debug(f"Multiplication result: {result}")
    return result


@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers. a and b and return the result."""
    logger.debug(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero.")
    result = a / b
    logger.debug(f"Division result: {result}")
    return result
