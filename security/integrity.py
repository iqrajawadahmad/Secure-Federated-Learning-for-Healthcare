import hashlib
import hmac
from security.config import SECRET_KEY
import hashlib

def hash_weights(weights):
    hasher = hashlib.sha256()
    for w in weights:
        hasher.update(w.tobytes())  # ✅ CRITICAL FIX
    return hasher.hexdigest()

def sign_update(payload):
    return hmac.new(SECRET_KEY, payload.encode(), hashlib.sha256).hexdigest()

def verify_signature(payload, signature):
    expected = sign_update(payload)
    return hmac.compare_digest(expected, signature)
