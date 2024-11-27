const anchor = require('@project-serum/anchor');
const { Connection, Keypair } = require('@solana/web3.js');

(async () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.IotDataStorage;

  // Replace with your deployed program's account and your test wallet
  const storageAccount = new Keypair();
  const device_id = "device_123";
  const timestamp = Date.now();
  const cid = "your_ipfs_cid_here";

  const tx = await program.rpc.storeData(device_id, timestamp, cid, {
    accounts: {
      storage: storageAccount.publicKey,
      owner: provider.wallet.publicKey,
      systemProgram: anchor.web3.SystemProgram.programId,
    },
    signers: [storageAccount],
  });

  console.log("Transaction Signature:", tx);
})();
