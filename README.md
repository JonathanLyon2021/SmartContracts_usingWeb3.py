# SmartContracts_usingWeb3.py
This is exercise 17 from MI4 @ Kingsland Universities Blockchain Developer Program.

# Goals
In this exercise, we will use web3.py library for interacting with Ethereum. Its API is derived from the Web3.js
JavaScript API and should be familiar to anyone who has used web3.js. The exercise will show how to interact with
an already deployed contract on the Ethereum Goerli Testnet.

1. Set up environment
Web3.py requires Python 3. It can be installed using pip as follows.
For this exercise we will use web3 5.29.0.
pip install web3
Create a new Python file and import the following:

We will need HTTPProvider in order to create our connection to the Goerli Testnet using Infura.io.
Now let’s get the necessary Infura.io provider. Go to https://infura.io/ and click [Get started for free]:

Fill out the form and click [Submit]. Then copy the Ropsten URL:

Page 2 of 11 https://kingslanduniversity.com
In order to get a contract instance of an already deployed contract, we will need its address and application binary
interface. For exercise’s purpose, deploy a simple contract storing an array of facts through Remix IDE using
MetaMask Goerli a provider.
