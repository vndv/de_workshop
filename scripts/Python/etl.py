import mysql.connector
import psycopg2
from psycopg2 import connect
from mysql.connector import errorcode
from clickhouse_driver import Client
from db_credentials import pg_db_config,my_sql_db_config,clickhouse_db_config

settings = {'input_format_null_as_default': True, 'types_check': True}

class ETLBase:
    def __init__(self,connection_source,target_table,target_schema):
        self.connection_source=connection_source,
        self.target_table=target_table,
        self.target_schema=target_schema,
        self.target_table=target_table,
        self._connection_object = None

    def _source_connect(self):
        if self.connection_source[0] == 'mysql':
            try:
                print('Connecting to the MY_SQL database...')
                self._connection_object = mysql.connector.connect(**my_sql_db_config)
                return self._connection_object
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
        if self.connection_source[0] == 'postgres':
            try:
                print('Connecting to the PostgreSQL database...')
                self._connection_object = connect(**pg_db_config)
                return self._connection_object
            except (Exception, psycopg2.DatabaseError) as err:
                print(err)


    def _dwh_connect(self):
        client = Client(**clickhouse_db_config,settings=settings)
        return client

    def do_insert(self,sql):
        clickhouse_client = self._dwh_connect()
        conn = self._source_connect()
        
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        clickhouse_client.execute(f"INSERT INTO {self.target_schema[0]}.{self.target_table[0]}  VALUES",
                            ((cur)for cur in data)
                                )
        
        cursor.close()
    



