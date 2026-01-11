# database.py

from langchain_community.utilities import SQLDatabase
from sql_agent.config import DB_URI
from sqlalchemy import inspect


def get_database():
    return SQLDatabase.from_uri(
        DB_URI,
        sample_rows_in_table_info=3
    )

def get_table_columns(table_name: str):
    engine = get_database()._engine
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    return [col["name"] for col in columns]

def build_table_columns():
    db = get_database()
    tables = list(db.get_usable_table_names())
    return {table: get_table_columns(table) for table in tables}