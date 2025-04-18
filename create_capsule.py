from config import CONTRACT, ACCOUNT, w3
from utils import send_transaction
from time import time

msg_hash = input("Enter hash of the message/file: ")
unlock_in = int(input("Unlock after how many seconds?: "))
unlock_time = int(time()) + unlock_in

tx = CONTRACT.functions.createCapsule(msg_hash, unlock_time).buildTransaction({
    "from": ACCOUNT.address,
    "nonce": w3.eth.get_transaction_count(ACCOUNT.address),
    "gas": 150000
})

tx_hash = send_transaction(tx)
print("✅ Capsule created:", w3.toHex(tx_hash))
