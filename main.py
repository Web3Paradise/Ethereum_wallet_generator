from eth_account import Account
from web3 import Web3
from web3.auto import w3
from eth_account import messages

# Connect to Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Generate 100 Ethereum wallets
wallets = []
for _ in range(100):
    acct = Account.create()
    private_key = acct.privateKey.hex()
    address = acct.address
    mnemonic_phrase = Account.from_key(private_key).create_signing_key().mnemonic
    wallets.append({
        "address": address,
        "private_key": private_key,
        "mnemonic": mnemonic_phrase
    })

# Print the wallets
for i, wallet in enumerate(wallets, 1):
    print(f"Wallet {i}:")
    print(f"Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    print(f"Mnemonic: {wallet['mnemonic']}")
    print()
