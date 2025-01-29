from pathlib import Path
import pandas as pd
import sqlite3

current_directory = Path(__file__).resolve().parent

filename = "chinook.db"

try:
    with sqlite3.connect(current_directory / "data" / filename) as connection:
        customers = pd.read_sql("SELECT * FROM customers", con=connection)
        invoices = pd.read_sql("SELECT * FROM invoices", con=connection)
    result = pd.merge(customers, invoices, on="CustomerId")

    print(result.groupby("CustomerId")["CustomerId"].count())

except FileNotFoundError as e:
    print("File not found")

except Exception as e:
    print(e)