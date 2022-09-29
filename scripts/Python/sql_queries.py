from clickhouse_driver import Client
from db_credentials import clickhouse_db_config

client = Client(**clickhouse_db_config)

print(client.execute('SHOW DATABASES'))
