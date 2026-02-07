import numpy as np

from security.secure_channel import prepare_secure_update
from security.secure_aggregation import verify_and_accept
from security.attack_simulation import malicious_update
from security.config import CLIENTS

# --------------------------------------------------
# STEP 1: Load trained model weights from notebook
# --------------------------------------------------
state = np.load("trained_weights.npy", allow_pickle=True).item()

weights = [
    state["coef"],        # Logistic Regression coefficients
    state["intercept"]    # Logistic Regression intercept
]

print("\n[+] Loaded trained model weights from notebook")

# --------------------------------------------------
# STEP 2: Legitimate hospital update
# --------------------------------------------------
client_id = "Hospital_A"
token = CLIENTS[client_id]

secure_update = prepare_secure_update(client_id, weights)

print("[+] Secure update prepared by Hospital_A")

accepted_weights = verify_and_accept(secure_update, token)

if accepted_weights is not None:
    print("✅ Legitimate update ACCEPTED\n")
else:
    print("❌ Legitimate update REJECTED\n")

# --------------------------------------------------
# STEP 3: Model poisoning attack
# --------------------------------------------------
print("[!] Simulating model poisoning attack...")

malicious_weights = malicious_update(weights)

malicious_packet = {
    "client_id": "Hospital_A",
    "weights": malicious_weights,
    "hash": secure_update["hash"],
    "signature": secure_update["signature"]
}

rejected = verify_and_accept(malicious_packet, token)

if rejected is None:
    print("🛑 Malicious update REJECTED (SECURITY WORKING)\n")
else:
    print("⚠️ Malicious update ACCEPTED (SECURITY FAILED)\n")

# --------------------------------------------------
# STEP 4: Fake hospital attack
# --------------------------------------------------
print("[!] Simulating fake hospital attack...")

fake_update = prepare_secure_update("Fake_Hospital", weights)
fake_result = verify_and_accept(fake_update, "FAKE_TOKEN")

if fake_result is None:
    print("🛑 Fake hospital BLOCKED (AUTH WORKING)\n")
else:
    print("⚠️ Fake hospital ACCEPTED (SECURITY FAILED)\n")

print("📄 Check 'security_logs.txt' for audit trail")
