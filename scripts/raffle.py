from typing import Dict, List, Set
from random import choice
from scripts import io_service
from scripts.snapshot import get_addresses_that_have_voted
from scripts.io_service import load_data
from scripts.nft import filter_addresses_with_nfts
from scripts.util import ordinal, get_address_to_ens_mapping
import os

def draw(address_list:List[str], number_of_winners:int = 125) -> Set:
    if address_list:
        number_of_winners = number_of_winners if number_of_winners < len(address_list) else len(address_list) 
        winners = []
        for i in range(1, number_of_winners+1):
            winner = choice(address_list)
            print(f"The {ordinal(i)} winner is {winner}")
            address_list.remove(winner)
            winners.append(winner)
        return winners
    return set()
        

def main(input_file_path:str='./test_file/address.csv', output_file_path:str='winners.csv', address_col_name:str="address", number_of_winners:int = 125):
    try:
        # Validate input file path
        if not input_file_path or not os.path.exists(input_file_path):
            raise ValueError(f"Please provide a valid file path for the CSV . Path {input_file_path} does not exists")

        print(f"Reading {input_file_path} where wallet address column name is {address_col_name}")

        # read given file and returns a mapping of valid deduped address to ens
        addess_to_ens_mapping:Dict[str, str] = load_data(input_file_path, address_col_name)
        addresses_to_check:List[str] = list(addess_to_ens_mapping.keys())
        print(f"{len(addresses_to_check)} unique addresses in file.")

        # filters the addresses that own atleast one of the citizen NFTs
        nft_holders:Set[str] = filter_addresses_with_nfts(addresses_to_check)
        if not len(nft_holders):
            raise ValueError("Cannot continue, as none of the addresses hold the citizen NFT.")
        print(f"Found {len(nft_holders)} addresses holding one or more citizen NFTS.")

        # filters the addresses that have voted atleast once thru snapshot
        eligible_addresses = get_addresses_that_have_voted(list(nft_holders))
        if not len(eligible_addresses):
            raise ValueError("Cannot continue, as none of the addresses have voted atleast once.")
        print(f"Found {len(eligible_addresses)} addresses that have voted atleast once.")

        # Randomly choose winners
        winners = draw(list(eligible_addresses))

        # Map winner addresses back to ens handle if provided in csv
        output_data = get_address_to_ens_mapping(winners, addess_to_ens_mapping)
         # Write the list of winners out to CSV file
        io_service.write_results(output_data, output_file_path)
    except Exception as ex:
        print(ex)
        raise ex
    