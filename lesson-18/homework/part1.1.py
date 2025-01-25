from pathlib import Path
import pandas as pd
import sqlite3

current_directory = Path(__file__).resolve().parent

filename = current_directory / 'data/chinook.db'

try:
    with sqlite3.connect(filename) as connection:
        customers = pd.read_sql(
            "SELECT * FROM customers",
            con=connection
        )

    print(customers.head(10))
except:
    print("Error occured")