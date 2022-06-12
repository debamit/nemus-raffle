# nemus-raffle
DAO raffle to select 125 random winners.


## Installation and Setup

1. Tested using Python 3.8.10. Recommend installing pyenv to manage python version.
Installation instruction regarding pyenv found here https://github.com/pyenv/pyenv

2. Run `pip install -r requirements.txt` (Only one dependency on `eth-brownie`)

3. Sign up for [Infura](https://infura.io/) and generate an API key. Store it in the `WEB3_INFURA_PROJECT_ID` environment variable. You can [learn more about environment variables here](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). If you're unfamiliar with environment variables you can just add all these commands to your `.env` file and run `source .env` when you're done. 

```bash
export WEB3_INFURA_PROJECT_ID=YourProjectID
```

## Testing
To make sure everthing is setup as expected run test
To run the tests:

```
brownie test
```

## To run the main script
```bash
$ brownie run scripts/raffle.py --network mainnet-fork
```