from brownie import interface, config
from scripts.nft import filter_addresses_with_nfts


def test_when_all_addresses_own_nft():
    addresses = ["0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F", 
            "0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B", 
            "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47", 
            "0x77aA943A365161e499eaFF59E936a799e6051e15"]
    owners=filter_addresses_with_nfts(addresses)
    print(owners)
    assert len(owners) == 4

def test_when_some_addresses_own_nft():
    addresses = ["0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F", 
            "0x598629CF97198821D069E9Bd0234e063BC0bd718", 
            "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47", 
            "0x77aA943A365161e499eaFF59E936a799e6051e15"]
    owners=filter_addresses_with_nfts(addresses)
    print(owners)
    assert len(owners) == 3

def test_when_no_addresses_own_nft():
    addresses = ["0x598629CF97198821D069E9Bd0234e063BC0bd718"]
    owners=filter_addresses_with_nfts(addresses)
    print(owners)
    assert len(owners) == 0


def test_nfts():
    addresses = ['0x98D78E1709657F502520FCD2Cf9665B15D95631c', '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC', '0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F', '0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B', '0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47', '0x77aA943A365161e499eaFF59E936a799e6051e15']
    owners=filter_addresses_with_nfts(addresses)
    print(owners)