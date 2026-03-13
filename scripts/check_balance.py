from web3 import Web3

rpc_url = "https://rpc.ankr.com/eth"
w3 = Web3(Web3.HTTPProvider(rpc_url))

address = "0x0000000000000000000000000000000000000000"

balance = w3.eth.get_balance(address)

print("Balance:", w3.from_wei(balance, "ether"), "ETH")
