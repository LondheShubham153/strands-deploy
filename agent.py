from strands import Agent
from strands.models.ollama import OllamaModel
import os

ollama_host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")

ollama_model = OllamaModel(model_id="llama3", host=ollama_host)

agent = Agent(model=ollama_model)

agent("Show me the Roadmap for Learning DevOps in 3 months, be precise and to the point, use 3-4 lines max!")
