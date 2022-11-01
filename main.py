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
