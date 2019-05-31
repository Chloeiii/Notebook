## :penguin:Blockchain and Ethereum 
---- 
#### prerequisites: 
 - distributed computing
 - data structures
 - application development
---- 
#### definition:

Ethereum:  

    A decentralized, open-source, public blockchain-based platform featuring contract functionality
    (supports smart contract)  

smart contract:   

    A protocol to digitally specify, verify, or enforce the terms of a contract.

Ethereum virtual machine:  

    A protocol to digitally specify, verify, or enforce the terms of a contract. 
    enable the excution of the smart contract code.

Blockchain:  

    Is a list of records that are stored across a sequence of blocks that are chained together using cryptography.
    
----     
Blockchain characteristics
  - continuously growing
  - maintained by a network of nodes
  - mechanism for nodes to reach consensus
  - records are immutable (cannot be edited or moved)
  - records are verifiable
  
 Ethereum (a blockchain network)
  - decentralized: not maintained by a single node, but by multiple nodes
  - open-source
  - public blockchain network (anyone can join)
  - smart contract functionality (you can define any kind of transaction. e.g. transfer of assets, implementation of a voting system)
  
Ethereum characteristics:
- block-chain based platform
- community of developers (new features and bug resolvment)
- anyone can join network
- mechanism to work with untrusted nodes
- EVM to run smart contracts (like java virtual machine)

What is a smart contract?
- a piece of excutable code
- defines contractual terms
- deployed to a blockchain network and everyone can see
- can be self-executing and self-enforcing
- invokes transactions

----
#### Mining and Ether

Mining: 

    The process of solving a complex mathematical puzzle 
    in order to earn the privilege of adding a block of transactions to the blockchain.    

- mining nodes verify transactions
- Uses significant amounts of compute resources (mining nodes can incur very high electricity costs, in addition to maintain the hardware )
- Miners need to be compensated

Ether:
  
    cryptocurrency for Ethereum (to pay out fees for transactions which are invokes from custom smart contracts.)
    1 Ether = $130 
    
- transaction originators pay a fee in Ethers to miner
- fee proportional to compexity of a transaction

- complexity measured in therms of gas
----
#### Chaining of blocks
how to insure all of the records are immutable and verifiable?   

Each block contains:
1. cryptographic hash of previous block
2. timestamp
3. transaction data

Transaction data in the block can't be altered after-the-act
- except by altering all subsequent blocks, which is complicated and requires consensus (getting this consesus is almost impossible)

----
#### Distributed Ledger
All of the entities which need access to that ledger will maintain their own copies of it. But we'll need to insure the consistancy of each ledger. in this case, all the nodes need to constantly communication with each other. -> a blockchain network.  
-> need Ethereum Victual Machine
EMS is responsible for
1. Exceting contract code
2. Calculating transaction complexity
3. verify transactions 

Each node has a key pair
- private key: used to sign (encrypt)
- public key: used to verify (decrypt)

    
