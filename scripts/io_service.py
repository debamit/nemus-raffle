import csv
from web3 import Web3
from scripts.util import get_unique_addresses
from typing import Dict
import os

def load_data(file_path:str, address_col_name:str="address") -> Dict:
    try:
        if os.path.exists(file_path):
            with open(file_path, mode='r') as csv_file:
                csv_content = csv.DictReader(csv_file) 
                return get_unique_addresses(csv_content)
    except IOError:
        print("I/O error")



def write_results(data_to_write:Dict, output_filename:str="winners.csv", columns=  ['address','ens']):
    try:
        with open(output_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in data_to_write:
                writer.writerow(data)
    except IOError:
        print("I/O error")