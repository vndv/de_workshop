class ETLBase:
    def __init__(
        self, target_table, target_schema, source_schema=None, source_table=None
    ):
        self.target_table = (target_table,)
        self.target_schema = (target_schema,)
        self.target_table = (target_table,)
        self.source_schema = (source_schema,)
        self.source_table = source_table

    def do_insert(self, dwh_con, source_con, sql):
        clickhouse_client = dwh_con
        conn = source_con

        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        clickhouse_client.execute(
            f"TRUNCATE TABLE {self.target_schema[0]}.{self.target_table[0]} "
        )

        clickhouse_client.execute(
            f"INSERT INTO {self.target_schema[0]}.{self.target_table[0]}  VALUES",
            ((cur) for cur in data),
        )

        cursor.close()

    def clickhouse_copy(self, dwh_con, source_con, sql):
        clickhouse_client = dwh_con
        conn = source_con

        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        clickhouse_client.execute(
            f"INSERT INTO {self.target_schema[0]}.{self.target_table[0]}  VALUES", data
        )

        cursor.close()
