from clickhouse_driver import Client
import mysql.connector
from db_credentials import my_sql_db_config, clickhouse_db_config

clickhouse_client = Client(**clickhouse_db_config)
con = mysql.connector.connect(**my_sql_db_config)


cursor = con.cursor()

my_sql_extract = """
SELECT
    Rerurned
    ,Order_id
FROM
    returns
"""

cursor.execute(my_sql_extract)

clickhouse_client.execute("INSERT INTO SAE.returns (Rerurned,Order_id) VALUES",
                         ((Rerurned,Order_id ) for Rerurned,Order_id in cursor))

cursor.close()
con.close()