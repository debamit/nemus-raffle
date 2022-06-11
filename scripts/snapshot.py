from brownie import accounts, network, Contract
from python_graphql_client import GraphqlClient
from typing import List, Set

client = GraphqlClient(endpoint="https://hub.snapshot.org/graphql")

query = """
    query Votes {
  votes (
    first: 10
    where: {
      space: "daocity.eth",
      voter_in: ["0x3B78Fcf6128D8903b4bDaB1e25244578b5A7676F", "0x3Fa79813b7b271f840b2242ed218E8235c3cAb5B", "0x67a06A59Fd7B8BB2ebf3aB5d33704Fd323e60a47", "0x77aA943A365161e499eaFF59E936a799e6051e15"]
    },
    orderBy: "voter",
    orderDirection: desc
  ) {
    id
    voter
    created
    choice
    space {
      id
    }
  }
}
"""

def get_addresses_that_have_voted(addresses:List[str]) -> Set:
    try :
        data = client.execute(query=query)
        voters = set(vote.get("voter") for vote in data.get("data").get("votes"))
        return voters  
    except Exception as ex:
        raise ex
