# The goal of this exercise is to read the object stored in data/testing/raw/data.json and save it 
# to the following path: data/testing/harmonized/data.json.
# 1. Inside the raw_to_harmonized folder, create a file called raw_to_harmonized.py
# 2. Write a function that reads the JSON files from data/testing/raw and transforms it to a 
# list of tuples, then returns this list together with the keys from the JSON object.
# 3. Write another function that takes as inputs a list of tuples, a list of strings, and a filepath. 
# The function should write the list as a JSON object to file.
# 4. Save the data as a file called data/testing/harmonized/data.txt

import json
import os
import pandas as pd


# CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# path_json = CURR_DIR_PATH + "raw/data.json"

# def transform_json(data):
#     path_json= open(path_json, "r")
#     data = json.load(path_json.read())
#     keys = list(data.keys())
#     values = list(data.values())
#     return keys, values

# keys, values = transform_json(path_json)

# # def write_json(keys, values, path_json):
# #     with open()


    


    
#### FUSKLAPP ####
path_json = 'C:\\code\\ETL-miniproject\\data\\testing\\raw\\data.json'


def read_json(path_json):
    with open(path_json) as f:
        data = json.load(f)
    return data

data = read_json(path_json)


def transform_json(data):
    keys = list(data.keys())
    values = list(data.values())
    return keys, values

keys, values = transform_json(data)


def write_json(keys, values, path_json):
    with open(path_json, 'w') as f:
        json.dump(dict(zip(keys, values)), f)

write_json(keys, values, path_json)



path_txt = r'C:\code\ETL-miniproject\data\\testing\\harmonized\data.txt'

def write_txt(keys, values, path_txt):
    with open(path_txt, 'w') as f:
        f.write(str(dict(zip(keys, values))))


write_txt(keys, values, path_txt)


