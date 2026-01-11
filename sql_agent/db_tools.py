from typing import List, ClassVar
from pydantic import BaseModel
from langchain.tools import BaseTool
from sql_agent.database import get_database, get_table_columns


# class ListTablesTool(BaseTool):
#     name: ClassVar[str] = "sql_db_list_tables"
#     description: ClassVar[str] = "List all tables in the database."

#     def _run(self, tool_input: str) -> List[str]:
#         db = get_database()
#         return list(db.get_usable_table_names())

#     async def _arun(self, tool_input: str):
#         raise NotImplementedError


# class TableSchemaInput(BaseModel):
#     table_name: str


# class TableSchemaTool(BaseTool):
#     name: ClassVar[str] = "sql_db_table_schema"
#     description: ClassVar[str] = "Get column names for a specific table."
#     args_schema: ClassVar[type] = TableSchemaInput

#     def _run(self, table_name: str):
#         return {table_name: get_table_columns(table_name)}

#     async def _arun(self, table_name: str):
#         raise NotImplementedError
