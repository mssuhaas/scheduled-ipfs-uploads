const { Connection, Keypair, LAMPORTS_PER_SOL } = require('@solana/web3.js');
const { Token, TOKEN_PROGRAM_ID } = require('@solana/spl-token');

const connection = new Connection('https://rpc.devnet.soo.network/rpc', 'confirmed');

const wallet = Keypair.generate();
console.log(`Wallet Public Key: ${wallet.publicKey.toBase58()}`);

async function airdrop() {
  const airdropSignature = await connection.requestAirdrop(wallet.publicKey, 2 * LAMPORTS_PER_SOL);
  await connection.confirmTransaction(airdropSignature);
  console.log('Airdropped 2 SOL to wallet for Devnet');
}

async function createToken() {
  const token = await Token.createMint(
    connection,
    wallet,
    wallet.publicKey, 
    null, 
    0, 
    TOKEN_PROGRAM_ID
  );
  console.log('Token Created on Devnet:', token.publicKey.toBase58());

  const tokenAccount = await token.createAssociatedTokenAccount(wallet.publicKey);
  console.log('Associated Token Account:', tokenAccount.toBase58());

  return token;
}

(async () => {
  await airdrop();
  const token = await createToken();

  const metadataUri = 'https://ivory-adorable-coyote-450.mypinata.cloud/ipfs/QmYSamuka5H7JsEqDPNE5f9wzePiEK9u94jxkLigjJKHBV';  // Replace with the actual metadata URL


  const tokenAccount = await token.createAssociatedTokenAccount(wallet.publicKey);
  await token.mintTo(tokenAccount, wallet.publicKey, [], 1000 * 10 ** 0);
  console.log('Minted Tokens to Associated Account');
})();
