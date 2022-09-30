from psycopg2 import connect
from clickhouse_driver import Client
from db_credentials import pg_db_config, clickhouse_db_config

settings = {'input_format_null_as_default': True, 'types_check': True}

pg_connection = connect(**pg_db_config)
clickhouse_client = Client(**clickhouse_db_config,settings=settings)

cur = pg_connection.cursor()

pg_extract = """select
  *
from
    public.orders;
"""

cur.execute(pg_extract)
result = cur.fetchall()

clickhouse_client.execute("INSERT INTO SAE.orders  VALUES",
                            ((res)for res in result)
                                )

cur.close()
pg_connection.close()