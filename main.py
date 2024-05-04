const fs = require('fs');

async function generateWallets() {
  const wallets = [];

  for (let i = 0; i < 100; i++) {
    const wallet = ethers.Wallet.createRandom();
    const address = wallet.address;
    const privateKey = wallet.privateKey;
    const mnemonic = wallet.mnemonic.phrase;

    wallets.push({
      address,
      privateKey,
      mnemonic,
    });
  }

  fs.writeFileSync('wallets.json', JSON.stringify(wallets, null, 2));
}

generateWallets();
