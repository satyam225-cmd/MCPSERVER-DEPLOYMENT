# MCP Server Deployment

A Model Context Protocol (MCP) server providing mathematical tools (subtract, multiply, divide) built with FastMCP and configured for easy deployment to remote servers.

## Features

- 🔧 Ready-to-use mathematical tools (subtract, multiply, divide)
- 📝 Environment-aware logging (development vs production)
- 🚀 Easy deployment to remote servers
- 📊 Automatic log rotation and retention
- 🎯 Built with FastMCP for high performance

## Prerequisites

### Local Development
- Python 3.14+
- [uv](https://github.com/astral-sh/uv) - Python package manager

### Remote Server
- Python 3.14+
- SSH access to remote server
- uv installed on remote server

## Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MCPSERVER-DEPLOYMENT
   ```

2. **Install dependencies**
   ```bash
   uv pip install -e .
   ```

   Or add packages individually:
   ```bash
   uv add mcp[cli] loguru
   ```

## Running the Server

### Local Development

**Standard Mode (Development)**
```bash
ENVIRONMENT=development LOG_LEVEL=DEBUG uv run mcp-server
```

**Production Mode**
```bash
ENVIRONMENT=production LOG_LEVEL=INFO uv run mcp-server
```

### With Inspector

Run the server with the built-in MCP Inspector for testing:
```bash
uv run mcp dev mcp-server
```

This will start the inspector on `http://localhost:5173` (or similar, check terminal output).

## Deploying to Remote Server

### Option 1: SSH + systemd Service (Recommended)

#### Step 1: Copy Project to Remote Server

```bash
# From your local machine
rsync -avz --exclude='.venv' --exclude='__pycache__' --exclude='logs' \
  ./ user@remote-server:/path/to/mcp-server
```

#### Step 2: Install on Remote Server

```bash
# SSH into remote server
ssh user@remote-server

# Navigate to project directory
cd /path/to/mcp-server

# Install dependencies
uv pip install -e .
```

#### Step 3: Create systemd Service

Create `/etc/systemd/system/mcp-server.service`:

```ini
[Unit]
Description=MCP Server
After=network.target

[Service]
Type=simple
User=<your-username>
WorkingDirectory=/path/to/mcp-server
Environment="ENVIRONMENT=production"
Environment="LOG_LEVEL=INFO"
Environment="LOG_FILE=/var/log/mcp-server/app.log"
ExecStart=/root/.local/bin/uv run mcp-server
Restart=always
RestartSec=10
StandardOutput=append:/var/log/mcp-server/app.log
StandardError=append:/var/log/mcp-server/app.log

[Install]
WantedBy=multi-user.target
```

#### Step 4: Start the Service

```bash
# Create log directory
sudo mkdir -p /var/log/mcp-server
sudo chown <your-username>:<your-username> /var/log/mcp-server

# Enable and start service
sudo systemctl enable mcp-server
sudo systemctl start mcp-server

# Check status
sudo systemctl status mcp-server

# View logs
tail -f /var/log/mcp-server/app.log
```

### Option 2: Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.14-slim

WORKDIR /app

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy project
COPY . .

# Install dependencies
RUN /root/.local/bin/uv pip install -e .

# Create logs directory
RUN mkdir -p logs

# Run server
ENV ENVIRONMENT=production
ENV LOG_LEVEL=INFO
ENV LOG_FILE=/app/logs/app.log

CMD ["/root/.local/bin/uv", "run", "mcp-server"]
```

Build and run:

```bash
# Build image
docker build -t mcp-server .

# Run container
docker run -v /path/to/logs:/app/logs \
  -e ENVIRONMENT=production \
  -e LOG_LEVEL=INFO \
  mcp-server
```

### Option 3: Direct Execution with nohup

```bash
# Connect to remote server
ssh user@remote-server

# Navigate to project
cd /path/to/mcp-server

# Run in background
nohup bash -c 'ENVIRONMENT=production LOG_LEVEL=INFO uv run mcp-server' > logs/output.log 2>&1 &

# Verify it's running
ps aux | grep mcp-server
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ENVIRONMENT` | `production` | Set to `development` for console logs, `production` for file-only logs |
| `LOG_LEVEL` | `INFO` | Log level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `LOG_FILE` | `logs/app.log` | Path to log file |

## Logs

Logs are automatically rotated when they reach 500MB and kept for 7 days.

**View logs:**
```bash
tail -f logs/app.log
```

## Available Tools

The server provides the following tools:

### subtract
Subtract two numbers.
- Parameters: `a: int`, `b: int`
- Returns: `int`

### multiply
Multiply two numbers.
- Parameters: `a: int`, `b: int`
- Returns: `int`

### divide
Divide two numbers.
- Parameters: `a: int`, `b: int`
- Returns: `float`
- Raises: `ValueError` if dividing by zero

## Troubleshooting

### Server won't start
1. Check logs: `tail logs/app.log`
2. Verify Python version: `python --version` (should be 3.14+)
3. Verify dependencies: `uv pip list`

### Connection refused on remote
1. Check if service is running: `sudo systemctl status mcp-server`
2. Check firewall: `sudo ufw status`
3. Allow port if needed: `sudo ufw allow 5000` (if using a specific port)

### Permission denied on logs
```bash
sudo chown -R <your-username>:<your-username> /var/log/mcp-server
```

## Development

### Running Tests

```bash
# Run tests (if implemented)
pytest
```

### Code Structure

```
src/mcpserver/
├── __init__.py           # Package init
├── __main__.py           # Entry point
├── deployments.py        # Tool definitions
├── logging_config.py     # Logging setup
└── add_numbers.py        # Additional tools
```

## License

[Add your license here]

## Support

For issues and questions, please open an issue or contact the maintainers.
