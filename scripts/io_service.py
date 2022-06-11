import csv
from web3 import Web3
from scripts.util import address_lookup, is_eth_handle
from typing import Dict

def load_data(file_path:str) -> Dict:
    def _get_unique_addresses(csv_content:Dict) -> Dict[str, str]:
        return {address_lookup(row.get("address")): row.get("address") 
                for row in csv_content 
                if Web3.isAddress(row.get("address", None)) or is_eth_handle(row.get("address"))}
    with open(file_path, mode='r') as csv_file:
        csv_content = csv.DictReader(csv_file) 
        return _get_unique_addresses(csv_content)

def write_results(data_to_write:Dict, output_filename:str="winners.csv"):
    try:
        columns = ['No','Name','Country']
        with open(output_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in data_to_write:
                writer.writerow(data)
    except IOError:
        print("I/O error")