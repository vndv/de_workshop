from core.etl import ETLBase
from queries.query_extract import pg_extract
from utils.connection_factory import dwh_connect, source_connect

orders = ETLBase("orders", "SAE", "public", "orders")

dwh = dwh_connect()
source = source_connect("postgres")

if __name__ == "__main__":
    orders.do_insert(dwh, source, pg_extract)
