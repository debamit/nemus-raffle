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
                if address_col_name not in csv_content.fieldnames:
                    raise ValueError(f"Column name {address_col_name} not found in file {file_path}")
                return get_unique_addresses(csv_content)
    except OSError:
        print(f'cannot read {file_path}')
        raise




def write_results(data_to_write:Dict, output_file_path:str="winners.csv", columns=  ['address','ens']):
    try:
        with open(output_file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in data_to_write:
                writer.writerow(data)
    except OSError:
        print(f'cannot write to path {output_file_path}. Please make sure that the path exists.')
        raise