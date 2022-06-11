from scripts import snapshot
import pytest

def test_voter_snapshot_when_all_have_voted():
    voters = ["0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F", 
            "0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B", 
            "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47", 
            "0x77aA943A365161e499eaFF59E936a799e6051e15"]
    result = snapshot.get_addresses_that_have_voted(voters)
    assert len(result) == 4


def test_voter_snapshot_when_some_have_voted():
    voters = ["0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F", 
            "0x598629CF97198821D069E9Bd0234e063BC0bd718", 
            "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47", 
            "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"]
    result = snapshot.get_addresses_that_have_voted(voters)
    assert len(result)  == 2 


def test_voter_snapshot_when_none_have_voted():
    voters = ["0x598629CF97198821D069E9Bd0234e063BC0bd718", 
            "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"]
    result = snapshot.get_addresses_that_have_voted(voters)
    assert len(result)  == 0 


def test_voter_snapshot_when_none_voter_list_is_empty():
    voters = []
    result = snapshot.get_addresses_that_have_voted(voters)
    assert len(result)  == 0 