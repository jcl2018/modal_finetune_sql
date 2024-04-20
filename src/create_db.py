from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    column,
    DateTime
)
from datetime import datetime

db_name = "word_beach_ios"

db_file = "{}.db".format(db_name)
engine = create_engine(f"sqlite:///{db_file}")
metadata_obj = MetaData()

# create SQL table
table_name = db_name
city_stats_table = Table(
    "word_beach_ios_app_launch",
    metadata_obj,
    Column("device_uuid", String),
    Column("created_at", DateTime(timezone=True)),
    Column("country", String))

metadata_obj.create_all(engine)

# insert sample rows
from sqlalchemy import insert

rows = [
    {"device_uuid": "ce15dca4ed06a0b178582e7e1a573f9e59bbf099", "created_at": datetime.strptime("09/19/22 13:55:26", '%m/%d/%y %H:%M:%S'), 'country': 'us'},
    {"device_uuid": "98bce8c95efd6e4ee64510145cb1a8db190e815a", "created_at": datetime.strptime("09/19/22 13:55:26", '%m/%d/%y %H:%M:%S'), 'country': 'uk'}
]
for row in rows:
    stmt = insert(city_stats_table).values(**row)
    with engine.connect() as connection:
        cursor = connection.execute(stmt)
        connection.commit()

# modal run src.inference_sql_llamaindex::main --query "How many devices have event 'APP_LOG' and event 'APP_EXIT'?" --sqlite-file-path "user_event.db"  --use-finetuned-model False
# llama_index.core.indices.struct_store.sql_query import NLSQLTableQueryEngine will convert input database to context text.

"""
You are a powerful text-to-SQL model. Your job is to answer questions about a database. You are given a question and context regarding one or more tables. 

You must output the SQL query that answers the question.

### Input:
Which city has the highest population?

### Context:
Table 'city_stats' has columns: city_name (VARCHAR(16)), population (INTEGER), country (VARCHAR(16)), and foreign keys:.

### Response:
SELECT city_name, population FROM city_stats ORDER BY population DESC LIMIT 1
"""
