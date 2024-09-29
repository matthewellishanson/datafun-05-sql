'''
Module 5 - This file will demonstrate basic usage of Python SQL integration.  It will:
- Create a database
- Fill that database with data
'''

#####################################
# Import modules
#####################################
import logging
import sqlite3
from pathlib import Path
import pandas as pd

#####################################
# Set up logging   
#####################################

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method


#####################################
# Define paths using joinpath
#####################################


db_file_path = Path.Path("project.db")
sql_file_path = Path.Path("sql").joinpath("create_tables.sql")
author_data_path = Path.Path("data").joinpath("authors.csv")
book_data_path = Path.Path("data").joinpath("books.csv")


#####################################
# Functions
#####################################

def verify_and_create_folders(paths): 
    """Verify and create folders if they don't exist, using paths as a list of paths where folders should be created."""
    for path in paths:
        folder = path.parent
        # create folder if it doesn't exist
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
            logging.info("Folder" + path + "created")
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist. db_path is where database should be created."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
        logging.info("Database created successfully")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables. db_path is where database should be created, sql_file_path is where the SQL file is located."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
            logging.info("Tables created successfully")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables. db_path is where database should be created, author_data_path is where the author data is located, book_data_path is where the book data is located."""
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
            logging.info("Data inserted successfully")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL statements from a file. db_filepath is where database should be created, sql_file is where the SQL file is located."""
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)   

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()