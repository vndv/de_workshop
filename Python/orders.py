from etl import ETLBase
from querise import pg_extract

orders = ETLBase('postgres','orders','SAE')

orders.do_insert(pg_extract)