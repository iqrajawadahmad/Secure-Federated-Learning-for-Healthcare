from security.integrity import hash_weights, sign_update

def prepare_secure_update(client_id, weights):
    payload = f"{client_id}:{hash_weights(weights)}"
    signature = sign_update(payload)

    return {
        "client_id": client_id,
        "weights": weights,
        "hash": hash_weights(weights),
        "signature": signature
    }

