from ens.auto import ns
from typing import Dict, List
from web3 import Web3


def is_eth_handle(ens_handle:str) -> bool:
    if ens_handle:
        return bool(ens_handle.endswith(".eth"))

def address_lookup(ens_handle:str) -> str:
    if is_eth_handle(ens_handle):
        return ns.address(ens_handle)
    return ens_handle

def get_unique_addresses(csv_content:List, address_col_name:str="address") -> Dict[str, str]:
    return {address_lookup(row.get(address_col_name)): row.get(address_col_name) 
            for row in csv_content 
            if (Web3.isAddress(row.get(address_col_name, None)) or is_eth_handle(row.get(address_col_name)))}

def get_address_to_ens_mapping(addresses, address_to_ens_mapping:Dict):
    return[{"address": address, "ens": address_to_ens_mapping.get(address)} for address in addresses]

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])