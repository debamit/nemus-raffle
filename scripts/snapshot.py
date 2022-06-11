from brownie import accounts, network, Contract
from python_graphql_client import GraphqlClient
from typing import List, Set

client = GraphqlClient(endpoint="https://hub.snapshot.org/graphql")

query = """
query Votes ($space: String, $voters: [String]){
  votes (
    first: 10
    where: {
      space: $space,
      voter_in: $voters
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

variables = {"space": "daocity.eth"}

def get_addresses_that_have_voted(addresses:List[str]) -> Set:
    try :
        if addresses:
          variables.update({"voters":addresses})
          data = client.execute(query=query, variables=variables)
          voters = set(vote.get("voter") for vote in data.get("data").get("votes"))
          return voters  
        return set()
    except Exception as ex:
        raise ex
