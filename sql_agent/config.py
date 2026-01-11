# config.py

# Your local Ollama model name
OLLAMA_MODEL = "gemma3:4b-it-qat"

# Context window — smaller models need lower contexts
NUM_CTX = 2048

# Ensure deterministic SQL generation
TEMPERATURE = 0

# Your SQLite path

VERBOSE = True

DB_URI = "sqlite:///data/Chinook_Sqlite.sqlite"
# DB_URI = "sqlite:///data/sqlite-sakila.db"
