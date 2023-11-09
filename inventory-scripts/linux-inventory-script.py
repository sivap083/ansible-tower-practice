#!/usr/bin/env python
import json

def read_inventory_from_file(file_path):
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

if __name__ == "__main__":
    inventory_data = read_inventory_from_file('./inventory-scripts/linux-json-payload.json')
    print(json.dumps(inventory_data, indent=4))