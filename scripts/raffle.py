from typing import Dict, List, Set
from random import choice
from scripts.snapshot import get_addresses_that_have_voted
from scripts.io_service import load_data
from scripts.nft import filter_addresses_with_nfts
from scripts.util import ordinal

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

def lfg(file_path:str='./test_file/address.csv', address_col_name:str="address"):
    print(f"Reading {file_path}")
    # read given file and returns a mapping of valid deduped address to ens
    addess_to_ens_mapping:Dict[str, str] = load_data(file_path, address_col_name)
    addresses_to_check:List[str] = list(addess_to_ens_mapping.keys())
    print(f"{len(addresses_to_check)} unique addresses in file.")
    # filters the addresses that own atleast one of the citizen NFTs
    nft_holders:Set[str] = filter_addresses_with_nfts(addresses_to_check)
    print(f"Found {len(nft_holders)} addresses holding one or more citizen NFTS.")
    # filters the addresses that have voted atleast once thru snapshot
    eligible_addresses = get_addresses_that_have_voted(nft_holders)
    print(f"Found {len(eligible_addresses)} addresses that have voted atleast once.")
    winners = draw(list(eligible_addresses))
    print(winners)