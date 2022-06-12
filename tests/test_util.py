import pytest
from scripts.util import address_lookup, get_unique_addresses
from web3 import Web3

def test_address_lookup_valid_ens():
    ens_handle = "vitalik.eth"
    address = address_lookup(ens_handle=ens_handle)
    print(address)
    assert Web3.isAddress(address)

def test_address_lookup_invalid_ens():
    ens_handle = "a.eth"
    address = address_lookup(ens_handle=ens_handle)
    print(address)
    assert Web3.isAddress(address) == False


def test_address_lookup_unclaimed_ens():
    ens_handle = "dfgaeryrehrstgjdtgjsrgaedfewagaergaerh.eth"
    address = address_lookup(ens_handle=ens_handle)
    print(address)
    assert Web3.isAddress(address) == False


def test_unique_address_when_duplicate_addresses():
    input = [{"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F"}, 
            {"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}, 
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}]
    unique_addresses = get_unique_addresses(input)
    print(unique_addresses)
    assert len(unique_addresses) == 3
    

def test_unique_address_when_duplicate_invalid_addresses():
    input = [{"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "0x3B78Fcf6128D8903b4bDaB1e252478b5A7676F"}, 
            {"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}, 
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}]
    unique_addresses = get_unique_addresses(input)
    print(unique_addresses)
    assert len(unique_addresses) == 2

def test_unique_address_when_invalid_addresses():
    input = [{"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "vitalik.eth"}, 
            {"address": "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"},
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}, 
            {"address": "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47"}]
    unique_addresses = get_unique_addresses(input)
    print(unique_addresses)
    assert len(unique_addresses) == 3

# def test_unique_address_when_invalid_ens_handle():
#     pass

def test_fix_bug():
    input=[{'address': 'debamit.eth', ' passion': ' something'}, 
    {'address': 'debamitdutta.eth', ' passion': ' whatever'}, 
    {'address': '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC', ' passion': ' account 2'}, 
    {'address': '0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F', ' passion': ' something'}, 
    {'address': '0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B', ' passion': ' something'}, 
    {'address': '0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47', ' passion': ' something'}, 
    {'address': '0x77aA943A365161e499eaFF59E936a799e6051e15', ' passion': ' something'}]
    unique_addresses = get_unique_addresses(input)
    print(unique_addresses)
    assert len(unique_addresses) == 6