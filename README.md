# Web3 Python Tools

A collection of simple Python scripts for interacting with blockchain networks using Web3.py.

This repository provides lightweight utilities for reading blockchain data, checking wallet balances, and sending transactions.

---

## Features

* Check wallet balance
* Send transactions
* Read smart contract data
* Fetch blockchain information

---

## Tech Stack

* Python
* Web3.py
* Requests
* python-dotenv

---

## Project Structure

```
web3-python-tools/
│
├── scripts
│   ├── check_balance.py
│   ├── send_transaction.py
│   └── read_contract.py
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/nicky79eth/web3-python-tools.git
cd web3-python-tools
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Usage

Run any script inside the `scripts` folder.

Example:

```
python scripts/check_balance.py
```

---

## Environment Variables

Create a `.env` file based on `.env.example`

```
cp .env.example .env
```

Then configure:

* RPC_URL
* PRIVATE_KEY
* WALLET_ADDRESS

---

## Future Improvements

* Token price checker
* Gas price monitor
* Wallet transaction scanner
* Block explorer script

---

## License

MIT
