from typing import List, Tuple, Set
from brownie import interface, config

nft_ids = [42, 69, 7]

def filter_addresses_with_nfts(addresses_to_check:List[str]) -> Set[str]:
    if len(addresses_to_check):
        address_to_ids:Tuple = tuple((address, id) for address in addresses_to_check for id in nft_ids)
        holders, ids = zip(*address_to_ids)
        citizen_contract=interface.ERC115Interface(config['networks']['mainnet-fork']['citizen_nft'])
        balances = citizen_contract.balanceOfBatch(holders, ids)
        holders_with_balance: Tuple=list(zip(holders, balances))
        return set(x[0] for x in holders_with_balance if x[1] > 0 )
    return set()