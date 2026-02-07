# Data Cleaning Pipeline

This project is a simple **data cleaning and loading pipeline**. It processes raw CSV data, cleans it using a Jupyter notebook, and loads it into a SQLite database for further analysis and querying.

---
## Project Structure

Data_Cleaning_Pipeline/
├── data/
│ ├── raw/
│ │ └── user_profiles_mesy.csv # Original raw CSV data
│ └── processed/
│ └── user_profiles_cleaned.csv # Cleaned CSV generated from notebook
├── SQLite/
│ ├── load_into_sql.py # Script to load CSV into SQLite
│ ├── user.db # SQLite database created by script
│ └── query.sql # SQL file with queries to check the table
├── data_cleaning-analysis.ipynb # Jupyter notebook used for cleaning the data
└── README.md # This documentation

---

## Workflow

1. **Raw Data**:  
   The raw CSV is `user_profiles_mesy.csv` located in `data/raw/`.

2. **Data Cleaning**:  
   The notebook `data_cleaning-analysis.ipynb` cleans the raw data and saves it as `user_profiles_cleaned.csv` in `data/processed/`.

3. **Loading into SQLite**:  
   The script `SQLite/load_into_sql.py`:
   - Reads the cleaned CSV from `data/processed/`.
   - Creates a SQLite database `user.db` in the `SQLite/` folder.
   - Creates a table `user_profiles` (if it does not exist).
   - Inserts all cleaned data into the table.

4. **Querying**:  
   `SQLite/query.sql` contains 3 queries that can be run to verify that the table `user_profiles` is loaded correctly.

## CSV Structure

The cleaned CSV has the following columns:

| Column        | Description                  |
|---------------|------------------------------|
| Id            | Unique user identifier       |
| Name          | Full name of the user        |
| Age           | Age of the user              |
| Signup_Date   | Date of signup (YYYY-MM-DD)  |
| Country       | Country of residence         |
| Salary_USD    | Salary in USD                |
| Active        | Account active status (True/False) |
| Email         | User email address           |

> Note: `Salary (USD)` in the original CSV is renamed to `Salary_USD` when loading into SQLite.

## Usage

1. Clean the raw data in the notebook:

```bash
    jupyter notebook data_cleaning-analysis.ipynb
```
2. Load the cleaned CSV into the SQLite database:
``` python SQLite/load_into_sql.py
```
3. Run queries to check the table:
```-- Open SQLite CLI or a DB browser
.read SQLite/query.sql
```

### Dependencies

- Python 3.x

- pandas

- sqlite3 (standard library)

- pathlib (standard library)

- Jupyter Notebook/Lab

## Notes

- The script automatically creates required folders (`data/processed` and `SQLite`) if they do not exist.
- The database `user.db` and the table `user_profiles` are stored in the `SQLite` folder, making it portable.
- `query.sql` can be customized to run additional checks or analysis queries on the `user_profiles` table.

# Author 
**morisak1**






