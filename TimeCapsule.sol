// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TimeCapsule {
    struct Capsule {
        address owner;
        string messageHash;
        uint256 unlockTime;
        bool revealed;
    }

    mapping(uint256 => Capsule) public capsules;
    uint256 public capsuleCount;

    event CapsuleCreated(uint256 capsuleId, address owner, uint256 unlockTime);
    event CapsuleRevealed(uint256 capsuleId, string messageHash);

    function createCapsule(string memory messageHash, uint256 unlockTime) external {
        require(unlockTime > block.timestamp, "Unlock time must be in the future");

        capsules[capsuleCount] = Capsule({
            owner: msg.sender,
            messageHash: messageHash,
            unlockTime: unlockTime,
            revealed: false
        });

        emit CapsuleCreated(capsuleCount, msg.sender, unlockTime);
        capsuleCount++;
    }

    function revealCapsule(uint256 capsuleId) external {
        Capsule storage c = capsules[capsuleId];
        require(block.timestamp >= c.unlockTime, "Capsule is still locked");
        require(!c.revealed, "Already revealed");

        c.revealed = true;
        emit CapsuleRevealed(capsuleId, c.messageHash);
    }

    function getCapsule(uint256 capsuleId) external view returns (address, string memory, uint256, bool) {
        Capsule memory c = capsules[capsuleId];
        return (c.owner, c.messageHash, c.unlockTime, c.revealed);
    }
}
