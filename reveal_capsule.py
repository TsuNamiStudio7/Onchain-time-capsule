from config import CONTRACT, ACCOUNT, w3
from utils import send_transaction

capsule_id = int(input("Capsule ID: "))

tx = CONTRACT.functions.revealCapsule(capsule_id).buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.get_transaction_count(ACCOUNT.address),
    "gas": 100000
})

tx_hash = send_transaction(tx)
print("🕰️ Revealed capsule:", w3.toHex(tx_hash))
