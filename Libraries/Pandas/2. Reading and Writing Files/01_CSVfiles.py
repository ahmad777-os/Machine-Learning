# Read CSV
import pandas as pd
df = pd.read_csv('pokemon.csv')
# Write CSV
df.to_csv("output.csv", index=False)

# read excel file
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
# Write Excel

df.to_excel("output.xlsx", index=False)


# Read JSON

df = pd.read_json("data.json")
# Write JSON

df.to_json("output.json", orient="records", lines=True)

# Read SQL

import sqlite3
conn = sqlite3.connect("mydb.sqlite")

df = pd.read_sql("SELECT * FROM users", conn)

# Read HTML

url = "https://www.example.com/table.html"
tables = pd.read_html(url)

print(tables[0])  # First table on the page