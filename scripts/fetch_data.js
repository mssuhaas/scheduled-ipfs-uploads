const anchor = require('@project-serum/anchor');

(async () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.IotDataStorage;

  const storageAccount = "StorageAccountPublicKey"; 

  const account = await program.account.deviceStorage.fetch(storageAccount);
  console.log("Stored Data:", account.records);
})();
