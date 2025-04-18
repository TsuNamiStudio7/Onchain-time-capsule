from solcx import compile_standard, install_solc
import json
from config import w3, ACCOUNT

install_solc("0.8.0")

def compile_and_deploy(sol_file, contract_name):
    with open(sol_file) as f:
        source = f.read()

    compiled = compile_standard({
        "language": "Solidity",
        "sources": {sol_file: {"content": source}},
        "settings": {"outputSelection": {"*": {"*": ["abi", "evm.bytecode"]}}}
    }, solc_version="0.8.0")

    abi = compiled["contracts"][sol_file][contract_name]["abi"]
    bytecode = compiled["contracts"][sol_file][contract_name]["evm"]["bytecode"]["object"]

    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx = contract.constructor().buildTransaction({
        "from": ACCOUNT.address,
        "nonce": w3.eth.getTransactionCount(ACCOUNT.address),
        "gas": 3000000
    })

    signed = ACCOUNT.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("✅ Deployed at:", receipt.contractAddress)

    with open("Capsule_abi.json", "w") as f:
        json.dump(abi, f, indent=2)

def send_transaction(tx):
    signed = ACCOUNT.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    w3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash
