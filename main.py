import psycopg2
import pandas as pd

dbname = 'mimiciv'

# local db has no authentication/user
# Connect to postgres with a copy of the MIMIC-IV database
con = psycopg2.connect(dbname=dbname)

query = """
SELECT subject_id, hadm_id, stay_id
FROM mimiciv_icu.icustays
LIMIT 10
"""
df = pd.read_sql_query(query, con)
df.head()