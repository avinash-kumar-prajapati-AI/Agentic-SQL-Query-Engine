from langchain_community.agent_toolkits import create_sql_agent
from langchain_classic.agents.agent_types import AgentType

from sql_agent.database import get_database
# from sql_agent.db_tools import ListTablesTool#, TableSchemaTool
from sql_agent.llm_factory import create_planner_llm


def create_agent():
    llm = create_planner_llm()
    db = get_database()

    agent = create_sql_agent(
        llm=llm,
        db=db,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        toolkit=None,
        extra_tools=[
            # SchemaLinkerTool(),     # <-- schema linker, try creating yours buddy
            # ListTablesTool(),        # <-- table lister, feel free to use this
        ]
    )
    return agent


def main():
    question = "how many customers whose email contains gmail."

    agent = create_agent()

    result = agent.invoke({"input": question})

    print("\n========= OUTPUT =======\n")
    print(result)


if __name__ == "__main__":
    main()
