from web3 import Web3
from eth_account import Account
from mnemonic import Mnemonic

# Connect to Ethereum mainnet node (replace with your mainnet provider URL)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Initialize Mnemonic class
mnemo = Mnemonic("english")

wallets = []
for _ in range(100):
    # Generate a new mnemonic
    mnemonic = mnemo.generate(strength=128)
    # Generate a seed from the mnemonic
    seed = mnemo.to_seed(mnemonic)
    # Create a wallet from the seed
    wallet = Account.from_mnemonic(mnemonic)
    # Extract address and private key
    address = wallet.address
    private_key = wallet.privateKey
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
