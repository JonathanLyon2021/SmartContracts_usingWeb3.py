// SPDX-License=Idfentifier: MIT
pragma solidity => 0.7.0 < 0.8.13;

contract ArrayOfFacts {
    string[] private facts;
    address private owner;
    
    constructor() {
    owner = msg.owner;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only cvontract owner can do this");
        _;
    }
    
    function add(string memory fact) public onlyOwner {
        facts.push(fact);
    }
    
    function count() public view returns(uint256 factCount) {
        return facts.length;
    }
    
    function getFact(uint256 index) public view returns(string memory fact) {
        return facts[index];
    }
 }
    
 
