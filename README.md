# Onchain Time Capsule

⏳ A decentralized time capsule using Ethereum smart contracts. Save data hashes that become viewable only after a future timestamp.

## Features

- 🔐 Hash-based storage for privacy
- 🕰️ Unlockable after specific time
- 🤖 Oracle auto-reveal support

## Files

- `TimeCapsule.sol` — smart contract
- `create_capsule.py` — store a message/file hash
- `reveal_capsule.py` — reveal after unlock time
- `oracle_clock.py` — auto-revealing daemon
- `view_capsule.py` — inspect capsule
- `deploy_contract.py` — deploy tool

## Example

```bash
python create_capsule.py
python reveal_capsule.py
python view_capsule.py
