import csv
from typing import Dict, Tuple, List, Set
from web3 import Web3
from typing import Dict
from ens.auto import ns
from brownie import Contract
from random import choice, sample
from snapshot import get_addresses_that_have_voted

# def test_read_csv_file():
#     with open('./test_file/address.csv', mode='r') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#             line_count += 1
#         print(f'Processed {line_count} lines.')

def draw(file_path:str='./test_file/address.csv'):
    print(f"Reading {file_path}")
    # return mapping of valid deduped address to ens from csv 
    addess_to_ens:Dict[str, str] = get_address_to_ens_from_file(file_path)
    addresses_to_check = list(addess_to_ens.keys())
    nft_ids = [42, 69, 7]
    print(f"Checking {len(addresses_to_check)} unique addresses to see if they hold Citizen NFT with ids {' , '.join(map(str, nft_ids))}")
    address_to_ids:Tuple = tuple((address, id) for address in addresses_to_check for id in nft_ids)
    holders, ids = zip(*address_to_ids)
    citi = Contract.from_explorer("0x7EeF591A6CC0403b9652E98E88476fe1bF31dDeb")
    balances = citi.balanceOfBatch(holders, ids)
    holders_with_balance: Tuple=list(zip(holders, balances))
    print(f"Found {len(holders_with_balance)} with holding one or more citizen NFTS")
    nft_holders = set(x[0] for x in holders_with_balance if x[1] > 0 )
    voting_addresses = get_addresses_that_have_voted(nft_holders)
    eligible_addresses = nft_holders.intersection(voting_addresses)
    winners = choose_winners(list(eligible_addresses))
    print(winners)


def get_address_to_ens_from_file(file_path:str) -> Dict:
    with open(file_path, mode='r') as csv_file:
        csv_content = csv.DictReader(csv_file) 
        return get_unique_addresses(csv_content)


def is_eth_handle(ens_handle:str) -> bool:
    if ens_handle:
        return bool(ens_handle.endswith(".eth"))

def address_lookup(ens_handle:str) -> str:
    if is_eth_handle(ens_handle):
        return ns.address(ens_handle)
    return ens_handle

def get_unique_addresses(csv_content:Dict) -> Dict[str, str]:
    return {address_lookup(row.get("address")): row.get("address") 
            for row in csv_content 
            if Web3.isAddress(row.get("address", None)) or is_eth_handle(row.get("address"))}

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

def choose_winners(address_list:List[str], number_of_winners:int = 2) -> Set:
    winners = []
    for i in range(1, number_of_winners+1):
        winner = choice(address_list)
        print(f"The {ordinal(i)} winner is {winner}")
        address_list.remove(winner)
        winners.append(winner)
    return winners
    

def draw_winner(address_list:List[str]):
    return choice(address_list)

# def get_unique_addresses(csv_content:Dict):
#     addresses = set()
#     for row in csv_content:
#         if Web3.isAddress(row.get("address")) or is_eth_handle(row.get("address")):
#             addresses.add(reverse_lookup_address(row.get("address")))
#     return addresses