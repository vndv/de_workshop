from etl import ETLBase
from querise import my_sql_extract

returns = ETLBase('mysql','returns','SAE')

returns.do_insert(my_sql_extract)