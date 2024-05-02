from eth_account import Account
from eth_account import mnemonic

# Generate 100 Ethereum wallets
wallets = []
for _ in range(100):
    acct = Account.create()
    private_key = acct.privateKey.hex()
    address = acct.address
    mnemonic_phrase = mnemonic.generate()
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
