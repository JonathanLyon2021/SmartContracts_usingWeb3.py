// SPDX-License=Idfentifier: MIT
pragmna solidity => 0.7.0 < 0.8.13;

contract ArrayOfFacts {
    string[] private facts;
    address private owner;
    
    constructor() {
    owner = msg.owner;
    }
    
    modifer onlyOwner() {
    require(msg.sender == owner, "Only cvontract owner can do this");
    _;
    }
    
