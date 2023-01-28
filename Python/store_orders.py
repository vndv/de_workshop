from core.etl import ETLBase
from utils.connection_factory import dwh_connect, source_connect
from queries.query_dds import (
    shipping_dim,
    customer_dim,
    product_dim,
    geo_dim,
    sales_fact,
)

dwh = dwh_connect()
source = source_connect("clickhouse")

table_list = {
    shipping_dim: "shipping_dim",
    customer_dim: "customer_dim",
    product_dim: "product_dim",
    geo_dim: "geo_dim",
    sales_fact: "sales_fact",
}

if __name__ == "__main__":
    for sql, table in table_list.items():
        instance = table + "_instance"
        instance = ETLBase(table, "DDS", "SAE", "orders")
        instance.clickhouse_copy(dwh, source, sql)
