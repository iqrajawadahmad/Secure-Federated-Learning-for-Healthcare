from security.auth import authenticate_client
from security.integrity import hash_weights, verify_signature
from security.logger import log_event

def verify_and_accept(update, token):
    client_id = update["client_id"]
    weights = update["weights"]


    if weights is None or len(weights) == 0:
        log_event(client_id, "EMPTY WEIGHTS REJECTED")
        return None

    payload = f"{client_id}:{update['hash']}"

    if not authenticate_client(client_id, token):
        log_event(client_id, "AUTH FAILED")
        return None

    if not verify_signature(payload, update["signature"]):
        log_event(client_id, "SIGNATURE INVALID")
        return None

    if hash_weights(weights) != update["hash"]:
        log_event(client_id, "HASH MISMATCH")
        return None

    log_event(client_id, "UPDATE ACCEPTED")
    return weights
