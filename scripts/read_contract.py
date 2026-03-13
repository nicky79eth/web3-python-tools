from web3 import Web3

rpc_url = "https://rpc.ankr.com/eth"
w3 = Web3(Web3.HTTPProvider(rpc_url))

contract_address = "0xContractAddress"

abi = []

contract = w3.eth.contract(address=contract_address, abi=abi)

print("Contract loaded:", contract_address)
