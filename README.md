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

4. Needs local installation of `ganache-cli`. [Ganache-CLI](https://github.com/trufflesuite/ganache-cli).




## Testing
To make sure everthing is setup as expected run test
To run the tests:

```
brownie test
```

## Expectations:
Valid CSV file, with atleast one record.

CSV with header column name matching the input argument.

Atleast 1 or more winners. In case of `number_of_winners` greater than than the number of addresses available. 

The number of winners will be equal to all the eligible addresses.

## To run the main script

There are 4 different arguments that you can pass to the main function .

`file_path` : absolute or relative file path of the CSV  (Default: './test_file/address.csv').

`output_file_path` : absolute or relative file path of the CSV  (Default: './test_file/address.csv').

`address_col_name` : column name which contains adresses or ens handles  (Default: 'address').

`number_of_winners` : number of winners that need to be selected  (Default: 125).

```bash
$ brownie run scripts/raffle.py main file_path output_file_path address_col_name number_of_winners --network mainnet-fork
```