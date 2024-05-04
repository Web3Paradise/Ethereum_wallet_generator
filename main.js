const ethers = require('ethers');
const fs = require('fs');

async function generateWallets() {
  const wallets = [];

  for (let i = 0; i < 100; i++) {
    const wallet = new ethers.Wallet.createRandom();
    const address = wallet.address;
    const privateKey = wallet.privateKey;
    const mnemonic = wallet.mnemonic.phrase;

    wallets.push(`Address: ${address}\nPrivate Key: ${privateKey}\nMnemonic: ${mnemonic}\n\n`);
  }

  const outputFile = 'wallets.txt';
  fs.writeFileSync(outputFile, wallets.join(''));
  console.log(`Wallets saved to ${outputFile}`);
}

generateWallets();
