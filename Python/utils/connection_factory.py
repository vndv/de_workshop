import mysql.connector
import psycopg2
from psycopg2 import connect
from mysql.connector import errorcode
from clickhouse_driver import Client, connect as cl_connect
from .db_credentials import pg_db_config, my_sql_db_config, clickhouse_db_config

settings = {"input_format_null_as_default": True, "types_check": True}


def source_connect(connection_source):
    if connection_source == "mysql":
        try:
            print("Connecting to the MY_SQL database...")
            connection_object = mysql.connector.connect(**my_sql_db_config)
            return connection_object
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    if connection_source == "postgres":
        try:
            print("Connecting to the PostgreSQL database...")
            connection_object = connect(**pg_db_config)
            return connection_object
        except (Exception, psycopg2.DatabaseError) as err:
            print(err)
    if connection_source == "clickhouse":
        print("Connecting to the Clickhouse database...")
        connection_object = cl_connect(**clickhouse_db_config, settings=settings)
        return connection_object


def dwh_connect():
    client = Client(**clickhouse_db_config, settings=settings)
    return client
