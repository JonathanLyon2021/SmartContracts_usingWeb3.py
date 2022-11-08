# SmartContracts_usingWeb3.py
In this exercise, we will use web3.py library for interacting with Ethereum. Its API is derived from the Web3.js
JavaScript API and should be familiar to anyone who has used **web3.js**. The exercise will show how to interact with
an already deployed contract on the Ethereum Goerli Testnet.

## 1. Set up environment
Web3.py requires Python 3. It can be installed using pip as follows.
For this exercise we will use web3 5.29.0.

      `pip install web3`
      
Create a new Python file.
We will need HTTPProvider in order to create our connection to the Goerli Testnet using Infura.io.
Now let’s get the necessary Infura.io provider. Go to *https://infura.io/* and click [Get started for free]:
Fill out the form and click [Submit]. Then copy the Goerli URL.
In order to get a contract instance of an already deployed contract, we will need its address and application binary
interface. For exercise’s purpose, deploy a simple contract storing an array of facts through Remix IDE using
MetaMask Goerli a provider.
Then, copy its address and ABI, and create an instance of the contract.

## 2. Writing to the Smart Contract
Now that there is an instance of the contract, create a method for writing facts in the smart contract. It will need the
instance, a private key/wallet, the address of the private key/wallet and the fact. The library is not recommended
to work with Local Private Keys in Production at the moment, so we will enable the unaudited features if needed.
Because the contract owner can only add facts to this contract, copy his private key and his address.
Copy the private key and the address. The address will be needed to easily calculate the nonce.
We will create a simple transaction, which adds a fact to the contract, sign it with the private key and send it.
Try adding a fact using another private key. The attempt will be unsuccessful because only the owner of the
contract can add facts.

## 3. Reading from the Smart Contract
When reading from a Smart Contract, no wallets or private keys are needed.
First, create a method which gets a fact by a given index.
Then create a method, which gets how many facts are stored in the contract.

### Congratulations! You've finished the exercise.
