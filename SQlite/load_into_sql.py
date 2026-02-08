from pathlib import Path as p # for file path handling
import sqlite3 # to query csv to Database
import pandas as pd # for data manipulation and loading csv to database

# Paths
csv_file = p(r"Data_Cleaning_pipline\data\processed") /"user_profiles_cleaned.csv"
db_file = p("Data_Cleaning_pipline\SQlite/user.db")  # DB in SQlite folder relative to script

# Ensure CSV and DB folders exist
csv_file.parent.mkdir(parents=True, exist_ok=True)
db_file.parent.mkdir(parents=True, exist_ok=True)

# Load CSV
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"CSV file not found at {csv_file}")
    exit()

# Connect to SQLite DB
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_profiles (
    Id TEXT PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Signup_Date TEXT,
    Country TEXT,
    Salary_USD REAL,
    Active BOOLEAN,
    Email TEXT
)
""")

# Insert CSV data into table
df.to_sql("user_profiles", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print(f"CSV loaded successfully into {db_file} -> table 'user_profiles'")
