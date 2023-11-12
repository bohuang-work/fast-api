import logging
import sys
from glob import glob

import psycopg2
from psycopg2 import sql

from postgresql_configs import PostgresqlConfig, load_postgresql_config


def execute_sql_file(connection, sql_file):
    try:
        with connection.cursor() as cursor:
            with open(sql_file, "r") as file:
                sql_commands = file.read().split(";")

                for command in sql_commands:
                    if command.strip():
                        cursor.execute(command)

        connection.commit()
        logging.info("Schema updated successfully.")
    except Exception as e:
        logging.error("Error updating schema:", e)
        connection.rollback()
        sys.exit(1)


def run_migration_up():
    # get postgresql configs
    configs: PostgresqlConfig = load_postgresql_config()

    # get SQL commands.
    sql_files = glob("files/*.up.sql")

    for sql_file in sql_files:
        try:
            logging.info(f"migrate {sql_file}")
            # Connect to the PostgreSQL database
            connection = psycopg2.connect(
                host=configs.host,
                port=configs.port,
                user=configs.user,
                password=configs.password,
                database=configs.database,
            )

            # Execute SQL commands from the file
            execute_sql_file(connection, sql_file)

        except psycopg2.Error as e:
            logging.error("Unable to connect to the database.")
            print(e)
            sys.exit(1)
        finally:
            if connection:
                connection.close()


if __name__ == "__main__":
    run_migration_up()
