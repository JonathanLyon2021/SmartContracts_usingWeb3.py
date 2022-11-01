from web3 import Web3, HTTPProvider

import json

PROVIDER = "https://goerli.infura.io/v3/08ca1c5dddd34508a9cba3a337ae801c"
w3 = Web3(HTTPProvider(PROVIDER))
#w3.eth.enable_unaudited_features();

CONTRACT_ADDRESS = "0xCfAFFFEd46B3f6ca362c847fb70F9b758a6E6eCD"

ABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "newFact",
				"type": "string"
			}
		],
		"name": "add",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "count",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "getFact",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

CONTRACT_INSTANCE = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI);

"""We create a simple transaction, which adds a fact to the contract, we sign it with the private key and send it."""
def add_fact(contract_instance, private_key, address, fact):
    noonce = w3.eth.getTransactionCount(address)
    add_transaction = contract_instance.functions.add(fact).buildTransaction({
        'gas': 4600000,
        'nonce': nonce
    })

    print(add_transaction)

signed_txn = w3.eth.account.signTransaction(add_transaction, private_key=private_key)
w3.eth.sendRawTransaction(signed_txn.rawTransaction)

fact = "The times 03/Jan/2009 Chancellor on brink of second bailout for banks"
add_fact(CONTRACT_INSTANCE, ACCOUNT3_PRIVATE_KEY, ACCOUNT3_ADDRESS, fact)

