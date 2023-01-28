from core.etl import ETLBase
from queries.query_extract import my_sql_extract
from utils.connection_factory import dwh_connect, source_connect

orders = ETLBase("returns", "SAE", "returns", "returns")

dwh = dwh_connect()
source = source_connect("mysql")

if __name__ == "__main__":
    orders.do_insert(dwh, source, my_sql_extract)
