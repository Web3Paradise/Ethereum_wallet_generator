from web3 import Web3
from eth_account import Account
import bip44
import secrets

# Connect to Ethereum mainnet node (replace with your mainnet provider URL)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

wallets = []
for _ in range(100):
    # Generate a new mnemonic for each wallet
    mnemonic = bip44.Wallet.new_random_wallet().mnemonic()
    # Create a wallet from the mnemonic
    wallet = bip44.Wallet(mnemonic)
    # Derive the first account from the wallet
    acct = wallet.derive_account("eth")
    # Extract address and private key
    address = acct.address()
    private_key = acct.private_key()
    # Append wallet details to the list
    wallets.append({
        "address": address,
        "private_key": private_key.hex(),
        "mnemonic": mnemonic
    })

# Print the wallets (be cautious with this in a real-world scenario)
for i, wallet in enumerate(wallets, 1):
    print(f"Wallet {i}:")
    print(f"Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    print(f"Mnemonic: {wallet['mnemonic']}")
    print()
