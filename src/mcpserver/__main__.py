from loguru import logger

from mcpserver.add_numbers import addmcp
from mcpserver.deployments import mcp
from mcpserver.logging_config import configure_logging


def main():
    # Configure logging
    configure_logging()
    logger.info("Starting MCP server")
    try:
        mcp.run()
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
