from etl import ETLBase
from querise import my_sql_extract

orders = ETLBase('mysql','returns','SAE')

orders.do_insert(my_sql_extract)