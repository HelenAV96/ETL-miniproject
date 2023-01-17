"""1. Inside the source_to_raw folder, create a file called source_to_raw.py
2. Write a function that does a request to a URL and returns the resource as a Python dict.
3. In the same file, write another function that takes a Python dict and a filepath and saves the 
dict as a JSON object in that path.
4. Wrap this up by calling the first function and use the result as input to the second function. 
The data should be stored in a file called data/testing/raw/data.json folder."""

import requests
import json
import os
import pandas as pd


swapi = "https://swapi.dev/api/"
list_of_resources = ["people", "planets", "films", "species", "vehicles", "starships"]

def get_resource(resource) -> dict:
    response = requests.get(swapi + resource + "/")
    return response.json()

def save_resource(resource, filepath):
    with open(filepath, "w") as file:
        json.dump(resource, file)

def get_and_save_resource(resource, filepath):
    resource = get_resource(resource)
    save_resource(resource, filepath)


def get_and_save_all_resources():
    for resource in list_of_resources:
        filepath = os.path.join("data", "testing", "raw", resource + ".json")
        get_and_save_resource(resource, filepath)



def combine_json_files():
    data = {}
    for resource in list_of_resources:
        filepath = os.path.join("data", "testing", "raw", resource + ".json")
        with open(filepath, "r") as file:
            data[resource] = json.load(file)
    filepath = os.path.join("data", "testing", "raw", "data.json")
    with open(filepath, "w") as file:
        json.dump(data, file)
    


get_and_save_all_resources()

combine_json_files()

