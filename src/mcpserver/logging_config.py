"""Logging configuration for MCP server."""

import os
import sys

from loguru import logger


def configure_logging():
    """Configure logging based on environment variables."""
    # Configuration from environment variables
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_file = os.getenv("LOG_FILE", "logs/app.log")
    environment = os.getenv("ENVIRONMENT", "production")

    # Remove default handler
    logger.remove()

    # Create logs directory if it doesn't exist
    os.makedirs(
        os.path.dirname(log_file) if os.path.dirname(log_file) else ".", exist_ok=True
    )

    # Add file handler
    logger.add(
        log_file,
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}",
        rotation="500 MB",
        retention="7 days",
    )

    # Add console handler (only in non-production)
    if environment != "production":
        logger.add(
            sys.stdout,
            level=log_level,
            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> | <level>{message}</level>",
        )

    logger.info(f"Logging configured - Environment: {environment}, Level: {log_level}")
    return logger
