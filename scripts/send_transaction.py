from web3 import Web3

rpc_url = "https://rpc.ankr.com/eth"
w3 = Web3(Web3.HTTPProvider(rpc_url))

private_key = "YOUR_PRIVATE_KEY"
account = w3.eth.account.from_key(private_key)

tx = {
    "to": "0x0000000000000000000000000000000000000000",
    "value": w3.to_wei(0.001, "ether"),
    "gas": 21000,
    "gasPrice": w3.to_wei("5", "gwei"),
    "nonce": w3.eth.get_transaction_count(account.address),
}

signed_tx = account.sign_transaction(tx)

tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Transaction sent:", tx_hash.hex())
