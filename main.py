from web3 import Web3
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.utils import generate_mnemonic
from typing import Optional

# Connect to Ethereum mainnet node (replace with your mainnet provider URL)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Generate English mnemonic words
MNEMONIC: str = generate_mnemonic(language="english", strength=128)

# Secret passphrase/password for mnemonic (optional)
PASSPHRASE: Optional[str] = None  # You can set your own passphrase

# Initialize Ethereum mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)

# Get Ethereum BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE)

# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

print("Mnemonic:", bip44_hdwallet.mnemonic())
print("Base HD Path: m/44'/60'/0'/0/{address_index}\n")

# Get Ethereum BIP44HDWallet information for the first 10 addresses
for address_index in range(10):
    # Derivation from Ethereum BIP44 derivation path
    bip44_derivation = bip44_hdwallet.get_derivation(account=0, change=False, address=address_index)

    # Print address_index, path, address, and private key
    print(f"({address_index}) {bip44_derivation.path()} {bip44_derivation.address()} 0x{bip44_derivation.private_key()}")

# Clean derivation indexes/paths
bip44_hdwallet.clean_derivation()
