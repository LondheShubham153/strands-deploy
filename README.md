# Strands Agents with Ollama

## Issue
`httpx.ConnectError: All connection attempts failed` when running Strands agent in Docker trying to connect to local Ollama.

## Root Cause
Docker containers can't reach `localhost` on the host machine - `localhost` refers to the container itself, not the host.

## Solution
Use `host.docker.internal` instead of `localhost` when running in Docker:

```python
ollama_host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
```

## Usage

### Prerequisites
- Ollama running locally on port 11434
- Docker installed

### Run with Docker
```bash
docker build -t strands-agent .
docker run --rm strands-agent
```

### Run locally (without Docker)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
OLLAMA_HOST=http://localhost:11434 python agent.py
```

## Files
- `agent.py` - Main agent code
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration
