# Agentic SQL Reasoner

An **agentic LLM-powered SQL reasoning framework** that follows a **Planner → Tool (SQL) → Synthesizer** architecture to answer complex natural-language questions over relational databases with dependency-aware planning, optimized SQL generation, and grounded natural-language explanations.

This project is designed for:

* NL → SQL with multi-step reasoning
* Dependency-aware analytical queries
* Explainable answers grounded only in database results
* Extensible skill-based agent systems (future: charts, forecasting, web search, etc.)

---

## ✨ Core Architecture

```
User Question
      ↓
[Planner LLM]
  - Refines intent
  - Reads schema
  - Decides: A valid SQL query
      ↓
[SQL Tool]
  - Executes SQL via LLM SQL Agent
      ↓
[Result]
  - Produces final grounded answer
```

### Components

| Component       | Role                                                       |
| --------------- | ---------------------------------------------------------- |
| Planner LLM     | Intent refinement, task decomposition, dependency planning |
| SQL Tool        | Executes schema-aware SQL using LLMs (Gemma/Qwen/DeepSeek) |
| Synthesizer LLM | Converts structured results into answer       |
| Orchestrator    | LangChain (now), LangGraph (future)                        |

---

## 📁 Project Structure

```
agentic-sql-reasoner/
│
├── main.py                # CLI entry point
├── data/
│   └── chinook.db         # Sample SQLite database
│
├── src/
│   ├── agent.py           # SQL Agent (LLM + create_sql_agent)
│   ├── config.py          # Model, temperature, DB URI
│   └── database.py        # SQLAlchemy / LangChain DB wrapper
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Prerequisites

### Hardware

* RAM: **16 GB minimum** (32 GB recommended)
* VRAM: **6 GB+ GPU** (for local LLMs via Ollama)
* OS: Windows 11 / Linux / macOS

### Software

1. **Python 3.10+**
2. **Ollama** (for local LLM inference)

Install Ollama:

Pull a supported model (example):

```bash
ollama pull gemma:4b-it
# or
ollama pull qwen2.5:7b
# or
ollama pull deepseek-r1:7b
```

---

## 🧪 Supported LLMs Modularizarion

| Model             | Role                            |
| ----------------- | ------------------------------- |
| Gemma 2/3 (4B–7B) | SQL generation (tool LLM)       |
| Qwen 2.5 / Qwen3  | Planner reasoning               |
| DeepSeek-R1       | Multi-step planning + synthesis |

---

## 🚀 Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourname/agentic-sql-reasoner.git
cd agentic-sql-reasoner
```

### 2. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Models

Edit `src/config.py`:

### 5. Run the Agent

```bash
uv run main.py
```

Then ask questions like these below:

```
1. how many customers whose email contains gmail?
2. Tell me first name of all customers whose email contains gmail?
3. Give me the City name of the first two customer?
```

---

## 🧠 Execution Flow

1. Planner analyzes intent and schema
2. Chooses:

   * optimized SQL based on LLM reasoning
3. SQL Tool executes queries
4. Results stored in structured state
5. Synthesizer LLM generates grounded explanation

---

## 🛡️ Design Principles

* No hallucination: answers only from SQL results
* Schema-aware reasoning
* Dependency-safe planning
* Explainable intermediate steps
* Extensible agent-tool architecture

## 🌟 Current limitations
* Not fully language aware and depend on the LLMS, hence using large LLM will give awesome result while small LMs like gemma3:4b etc only answer simple query.
* Highly complex queries involve CTEs, Subquery etc

