from config import CONTRACT

def test_capsule_view(capsule_id):
    owner, msg_hash, unlock_time, revealed = CONTRACT.functions.getCapsule(capsule_id).call()
    assert len(msg_hash) > 0
    assert unlock_time > 0
    print(f"Capsule {capsule_id} OK | Owner: {owner} | Revealed: {revealed}")

test_capsule_view(0)
