const ethers = require('ethers');

async function generateWallets() {
  const wallets = [];

  for (let i = 0; i < 100; i++) {
    const wallet = new ethers.Wallet.createRandom();
    const address = wallet.address;
    const privateKey = wallet.privateKey;
    const mnemonic = wallet.mnemonic.phrase;

    wallets.push({
      address: address,
      privateKey: privateKey,
      mnemonic: mnemonic
    });
  }

  console.log(JSON.stringify(wallets, null, 2));
}

generateWallets();
