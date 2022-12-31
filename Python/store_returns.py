from core.etl import ETLBase
from utils.connection_factory import dwh_connect,source_connect
from queries.query_dds import returns_fact

dwh = dwh_connect()
source = source_connect('clickhouse')

returns_table = ETLBase('returns_fact','DDS','SAE','returns')

if __name__ == '__main__':
    returns_table.clickhouse_copy(dwh,source,returns_fact)