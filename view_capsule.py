from config import CONTRACT

capsule_id = int(input("Capsule ID to view: "))
owner, message_hash, unlock_time, revealed = CONTRACT.functions.getCapsule(capsule_id).call()

print(f"Owner: {owner}\nUnlocks At: {unlock_time}\nRevealed: {revealed}\nMessage Hash: {message_hash}")
