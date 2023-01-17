# The goal of this exercise is to read the object stored in data/testing/harmonized/data.TXT and
# save it in the path data/testing/cleansed/data.json.
# 1. Inside the harmonized_to_cleansed folder, create a file called 
# harmonized_to_cleansed.py.
# 2. Create a function that reads a text file
# 3. Create a function that takes a Python dict and returns two values:
# ◦A list of its keys. We will use these as column names in the database table soon.
# ◦A list of tuples. If we are working with one dict at a time, then the list of tuples will only 
# have one item (one tuple) in itself.
# 4. Create a function that takes a list of strings, a list of tuples, a table schema and a table name. 
# This function should make an insert to a table in the cleansed schema in your database. 
import pandas as pd
import psycopg2

path_json = 'C:\\code\\ETL-miniproject\\data\\testing\\harmonized\\data.txt'

def read_file():
    data = pd.read_csv(path_json)
    return data


def transform_dict(data):
    keys = list(data.keys())
    tuples = list(data.tuples())
    return keys, tuples

def push_dict(tuples, strings, table_name, schema):
    strings = list(strings)
    tuples = list(tuples)
    conn= psycopg2.connect('archprep.db')
    c = conn.cursor()
    for tuple in tuples:
        c.execute(f'INSERT INTO {schema}.{table_name}") VALUES {tuple}')
    for string in strings:
        c.execute(f'INSERT INTO {schema}.{table_name}") VALUES {string}')
    conn.commit()
    conn.close()
    
