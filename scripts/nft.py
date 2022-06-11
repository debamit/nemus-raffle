from typing import List, Tuple, Set
from brownie import Contract

nft_ids = [42, 69, 7]

def filter_addresses_with_nfts(addresses_to_check:List[str]) -> Set[str]:
    address_to_ids:Tuple = tuple((address, id) for address in addresses_to_check for id in nft_ids)
    holders, ids = zip(*address_to_ids)
    citizen_contract = Contract.from_explorer("0x7EeF591A6CC0403b9652E98E88476fe1bF31dDeb")
    balances = citizen_contract.balanceOfBatch(holders, ids)
    holders_with_balance: Tuple=list(zip(holders, balances))
    return set(x[0] for x in holders_with_balance if x[1] > 0 )
