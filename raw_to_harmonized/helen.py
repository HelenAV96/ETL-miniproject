import json
import os

def read_json_dir_to_tuples(dir_path):
    tuples_list = []
    keys = []
    for filename in os.listdir(dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(dir_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                keys = list(data.keys())
                for key, value in data.items():
                    tuples_list.append((key, value))
    return tuples_list, keys