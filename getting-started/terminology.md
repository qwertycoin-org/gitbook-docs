# Terminology

## Consensus Related

* Proof of Work \(PoW\) - a blockchain consensus that involves mining for a reward system and security. 
* Proof of Stake \(PoS\) - a blockchain consensus that involves staking coins as a reward system and security 
* Delegated Proof of Stake \(DPoS\) - a blockchain consensus that involves staking and delegation of rights to a designated number of nodes 
* Egalitarian Proof of Work \(EPoW\) - a blockchain consensus that involves mining for an egalitarian reward system and security. 
* Egalitarian Proof of Service \(EPoSe\) - a blockchain consensus with a combination of EPoW and Uptime Nodes for egalitarian reward system and security. Qwertycoin\(QWC\)'s original concept. 

## Wallet Related

* Wallet - software that helps user to send/receive coins as well as keep transaction records + additional blockchain add-on features. 
* Wallet Address - an address derived from public key. Users can use an wallet address to receive payments from others or send coins from exchanges. 
* Public Key - a unique key used for generating a wallet address and transactions. A wallet address is derived from this key. Users can retrieve this information from wallet.
  * Users can retrieve this information from wallet. 
* Private Key - a unique key used in wallets. This key is unique per address and grants a full access to the respective wallet address. 
  * _**Keep it to yourself only and do not post or share it anyone.**_
  * Users can retrieve this information from wallet.
  * Users can import this key in wallet to get a full access including viewing and spending. 
* View Key - a unique key used to view the details including transactions of a wallet address. It can be shared, but do not recommend it. 
  * Users can retrieve this information from wallet.
  * Users can import this information in wallet to view details of its transactions and wallet address.  
* Spend Key - It is a synonym of private key. 

  * _**Keep it to yourself only and do not post or share it anyone.**_

  _\*\*\*\*_

* Mnemonic Seed - a sequence of words derived from a private key.
  * _**Keep it to yourself only and do not post or share it anyone.**_ 
* Churning - making a transaction from and to the same wallet address. 
* Full-Node Wallet -  a type of wallet that runs a node and a wallet within the same software; this type of wallet stores entire blockchain data with a wallet file and its transactions in local device. It does not require a remote connection to a public or private node since it uses its own node.   
  
  Pros: 

  * This is the most secure type of wallet.
  * Initial blockchain synchronization can take sometime since users can make transactions after block synchronization is finished. A snapshot of blockchain is available for download if users want to shorten this downtime.
  * Node service fee is waived.

  
  Cons: 

  * Users sacrifice time for block synchronization and a lot of disk space is required for storing entire blockchain. This wallet is not recommended for non-daily users.
  * This type of wallet is not practical for mobile and web platforms.
  * Slow internet speed or outdated computers can be problems.
  * A proper backup of private and/or mneumonic seeds is required for gaining a full access to a wallet address.

  

* SPV\(Simplified Payment Verification\) Wallet - a type of wallet that runs without a node; a remote connection to a public or private node is required to send/receive and record transactions. Only a wallet file and its transaction records are stored in local device.  


  Pros: 

  * This wallet provide good security measure.
  * No need for blockchain synchronization. Once connection to a remote node is established, users can send/receive payments.
  * Can also be developed as mobile and web platforms.
  * Even slow internet speed or outdated computers can work with this wallet.

  
  Cons: 

  * Node service fee has to be paid.
  * A proper backup of private and/or mneumonic seeds is required for gaining a full access to a wallet address.

  

* API Endpoint Wallet - a type of wallet that runs without a node; only keys are stored in the local device and delegates all other works to the wallet service provider.  


  Pros: 

  * No need for blockchain synchronization. Once connection to a remote node is established, users can send/receive payments.
  * Can also be developed as mobile and web platforms.

  
  Cons: 

  * This wallet provide the least security measure.
  * Wallet loading time takes forever. This is intrinsic to its structure.
  * Node service fee has to be paid.
  * Slow internet speed or insufficient server performance can be a problem.
  * Clearing browser cache will erase locally stored keys. A proper backup of private and/or mneumonic seeds is required for gaining a full access to a wallet address. 

* Offline Wallet - a type of wallet that runs without a node; only wallet address, key and/or mneumonic seeds information are provided.  


  Pros: 

  * Some considers this the most secure wallet.

  
  Cons: 

  * The wallet address can be used for receiving funds. To make a transaction, the wallet file must be imported through a wallet before use. 

* Snapshot - a blockchain file for download to speed up block synchronization process.

## Node Related

* Node - a software that verifies/holds transactions from wallet and stores block information. It is also called as a daemon. 
* Checkpoint - irreversible point of blockchain 
* Node Fee - amount of payment paid to node's registered wallet address when using remote node connection to make transactions from wallet  
* Uptime - a measure of time that a node has been providing service above minimum performance level to blockchain. Used for selecting  
* Memory Pool - a memory space used to temporarily store transactions until they are included in blocks.

## Mining Related

* Mining - a process of finding a complex problem by using computer resources including CPU, GPU, FGPA or ASIC. 
* Miner - a person or a a device that participates in mining activities. 
* Mining Software - software used for solving problems proposed by blockchain with PoW consensus. 
* CPU - an abbreviation of Core or Central Processing Unit of a computer \(Intel or AMD processors\) 
* GPU - an abbreviation of Graphics Processing Unit of a computer \(Nvidia or AMD\) 
* FPGA - an abbreviation of field-programmable gate array; an integrated circuit designed to be configured by a customer or a designer after manufacturing 
* ASIC - an abbreviation of application-specific integrated circuit; an integrated circuit chip customized for a particular use, rather than intended for general-purpose use 



