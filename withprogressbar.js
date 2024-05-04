const ethers = require('ethers');
const fs = require('fs');
const ProgressBar = require('progress');

async function generateWallets() {
  const wallets = [];
  const progressBar = new ProgressBar('Generating wallets [:bar] :percent', {
    complete: '=',
    incomplete: ' ',
    width: 20,
    total: 100,
  });

  for (let i = 0; i < 100; i++) {
    const wallet = new ethers.Wallet.createRandom();
    const address = wallet.address;
    const privateKey = wallet.privateKey;
    const mnemonic = wallet.mnemonic.phrase;

    wallets.push(`Address: ${address}\nPrivate Key: ${privateKey}\nMnemonic: ${mnemonic}\n\n`);
    progressBar.tick();
  }

  const outputFile = 'wallets.txt';
  fs.writeFileSync(outputFile, wallets.join(''));
  console.log(`\nWallets saved to ${outputFile}`);
}

generateWallets(); 
