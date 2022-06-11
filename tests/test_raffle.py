from unittest import result
import pytest
from scripts import raffle


def test_draw_address_list_greater_than_expected_winners():
    eligible_addresses = ['0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B', '0x77aA943A365161e499eaFF59E936a799e6051e15', "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"]
    number_of_winners = 2
    winners = raffle.draw(eligible_addresses, number_of_winners)
    assert len(winners) == number_of_winners

def test_draw_address_list_less_than_expected_winners():
    eligible_addresses = ['0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B', '0x77aA943A365161e499eaFF59E936a799e6051e15', "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"]
    number_of_winners = 10
    expected_winnners = len(eligible_addresses)
    winners = raffle.draw(eligible_addresses, number_of_winners)
    assert len(winners) == expected_winnners

def test_draw_when_address_list_is_empty():
    eligible_addresses = []
    number_of_winners = 10
    winners = raffle.draw(eligible_addresses, number_of_winners)
    assert len(winners) == 0