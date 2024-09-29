'''
Module 5 - This file will demonstrate basic usage of Python SQL integration.  It will:

- Manipulate that data by calling sql queries sorted into distinct files
'''

#####################################
# Import modules
#####################################
import logging
import sqlite3
from pathlib import Path
import pandas as pd

# Import execute_sql_file from db_operations_Hanson
from db_operations_Hanson import execute_sql_from_file

#####################################
# Global variables
#####################################

# Define database path 
db_file_path = Path("project.db")

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

#####################################
# Main function
#####################################

def main():
    # Define the SQL folder path
    sql_folder_path = Path("sql")

    # Define the SQL files to execute
    sql_files = [
        sql_folder_path.joinpath("create_tables.sql"),
        sql_folder_path.joinpath("insert_records.sql"),
        sql_folder_path.joinpath("update_records.sql"),
        sql_folder_path.joinpath("delete_records.sql"),
        sql_folder_path.joinpath("query_aggregation.sql"),
        sql_folder_path.joinpath("query_filter.sql"),
        sql_folder_path.joinpath("query_sorting.sql"),
        sql_folder_path.joinpath("query_group_by.sql"),
        sql_folder_path.joinpath("query_join.sql"),
    ]

    # Execute each SQL file
    for sql_file in sql_files:
        execute_sql_from_file(db_file_path, sql_file)
        
    logging.info(f"Executed SQL file: {sql_file}")

#####################################
# Conditional script execution
#####################################

if __name__ == "__main__":
    main()