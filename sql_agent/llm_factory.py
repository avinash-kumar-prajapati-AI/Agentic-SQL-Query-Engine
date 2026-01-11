from langchain_ollama import OllamaLLM
from sql_agent.config import NUM_CTX, TEMPERATURE

from langchain_core.language_models import BaseLanguageModel

MODELS = ['gemma3:4b-it-qat', 'deepseek-r1', 'llama3.2', 'llama3.1:8b']
SELECTED_MODEL = MODELS[0]

def create_planner_llm():
    return OllamaLLM(
        model=SELECTED_MODEL,
        base_url="http://127.0.0.1:11434",
        temperature=TEMPERATURE,
        num_ctx=NUM_CTX
    )
