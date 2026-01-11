# agent.py

from langchain_community.agent_toolkits import create_sql_agent
# from langchain_community.tools import 
from langchain_classic.agents.agent_types import AgentType

from sql_agent.database import get_database
from sql_agent.db_tools import ListTablesTool#, TableSchemaTool
from sql_agent.relevent_table_tool import SchemaLinkerTool
from sql_agent.llm_factory import create_planner_llm


def create_agent():
    # Initialize your local Ollama model
    llm = create_planner_llm()

    db = get_database()

    # Create a SQL agent that uses the model & db
    agent = create_sql_agent(
        llm=llm,
        db=db,
        # toolkit=None,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        extra_tools=[
            SchemaLinkerTool(), 
            # TableSchemaTool(), 
        ]
    )

    return agent
