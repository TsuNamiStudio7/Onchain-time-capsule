from view_capsule import CONTRACT
from reveal_capsule import send_transaction, w3, ACCOUNT

def check_and_reveal():
    count = CONTRACT.functions.capsuleCount().call()
    for i in range(count):
        _, _, unlock_time, revealed = CONTRACT.functions.getCapsule(i).call()
        if not revealed and unlock_time <= int(time.time()):
            print(f"⏳ Revealing capsule {i}")
            tx = CONTRACT.functions.revealCapsule(i).buildTransaction({
                "from": ACCOUNT.address,
                "nonce": w3.eth.get_transaction_count(ACCOUNT.address),
                "gas": 100000
            })
            tx_hash = send_transaction(tx)
            print(f"✅ Revealed {i}: {w3.toHex(tx_hash)}")

if __name__ == "__main__":
    import time
    while True:
        check_and_reveal()
        time.sleep(15)
