# Secure Federated Learning for Healthcare

## Project Overview

This project develops a secure and privacy-preserving Federated Learning (FL) framework for healthcare institutions that need to collaborate on machine learning without sharing raw patient data. In a sensitive domain such as healthcare, model training must balance predictive performance with confidentiality, trust, and robustness against cyber threats. This system addresses that challenge by securing the model update pipeline in an untrusted network environment.

The framework is designed for hospitals or clinical institutions that want to train a shared model collaboratively while preserving patient privacy. It protects against fake-client attacks, model poisoning, update tampering, and unauthorized participation, making the system relevant to real-world healthcare AI deployments.

---

## Why This Project Matters

Healthcare data is highly sensitive, regulated, and often fragmented across institutions. Traditional centralized training is not viable because it requires transferring patient records, which raises privacy, compliance, and security concerns. Federated Learning solves this by keeping data local while sharing only model updates.

However, FL systems are vulnerable to malicious updates and adversarial clients. This project strengthens the trust layer by validating every update before it influences the global model. In doing so, it demonstrates how secure AI systems can support privacy-preserving healthcare innovation without compromising integrity.

---

## Core Objectives

- Preserve patient privacy by avoiding raw data sharing
- Enable collaborative learning across multiple hospitals
- Detect tampering, replay, and malicious model updates
- Prevent unauthorized or fake clients from participating
- Maintain a verifiable audit trail for security analysis

---

## Technical Architecture

The system includes three main components:

1. Hospital clients that locally train model weights
2. A central server that aggregates verified updates
3. A security layer that authenticates, validates, and logs each transmission

The end-to-end flow is:

1. Each hospital trains a local model using private data
2. Model weights are hashed and signed before transmission
3. The server verifies client identity and update integrity
4. Only trusted updates proceed to aggregation
5. Security events are recorded in an audit log for traceability

---

## Machine Learning Notebook and Saved Weights

The `ct.ipynb` notebook uses scikit-learn's Logistic Regression with the breast cancer dataset. It trains a centralized model and also contains an experimental simulation that divides the data into three hospital groups and attempts to aggregate their model parameters.

The notebook's save cell writes the centralized model's `coef_` and `intercept_` to `trained_weights.npy`. The `run_demo.py` script loads these values and uses them as the weights in its secure-update, model-poisoning, and fake-client demonstrations. This file contains model parameters only; it does not contain patient records, the scaler, or the federated model's aggregated parameters.

The hospital split in the current notebook is experimental: the first hospital's consecutive data slice contains only class 0, but the initialization code searches that slice for both classes. As a result, the federated-training section may stop with an index error before it completes. The centralized model and saved-weight security demo are separate from that federated-training result.

---

## Security Mechanisms Implemented

### Client Authentication
Each hospital is assigned a unique client ID and secret token. The server validates the token before processing any update. This prevents unauthorized or fake institutions from contributing malicious data.

### Integrity Verification with SHA-256
Model weights are hashed before transmission, and the server recomputes the hash to confirm that the update has not been modified in transit. Any mismatch indicates tampering or corruption.

### Cryptographic Signing with HMAC
Each update is signed using HMAC with a shared secret key. Server-side validation checks the message authenticity and blocks forged or replayed updates.

### Secure Aggregation Gate
The validation layer enforces authentication, signature verification, and hash integrity checks before any model update is accepted into the aggregation process. This ensures only trustworthy updates influence the global model.

### Audit Logging
Every security decision is logged with the client ID, action type, and outcome. This provides traceability and supports forensic investigation and compliance-oriented monitoring.

---

## Threat Model

This project assumes an adversarial and untrusted network environment. The system is designed to defend against:

- Fake hospital or unauthorized client participation
- Update modification during transmission
- Model poisoning through malicious weights
- Forged or replayed update messages

The design follows a Zero Trust principle: no update is trusted by default and every incoming model is independently verified.

---

## Attack Simulation and Validation

The system was tested against simulated security threats:

- Malicious weights injected into a legitimate update were rejected after hash mismatch detection
- Fake hospital attempts were blocked due to authentication failure
- Tampered or forged updates were rejected before aggregation

These simulations validate that the security layer successfully filters out adversarial updates while preserving legitimate collaboration.

---

## Impact and Relevance

This project demonstrates a practical, industry-aligned solution for privacy-preserving machine learning in healthcare. It combines concepts from cybersecurity, distributed systems, and responsible AI to build a trustworthy FL pipeline for sensitive applications.

It is highly relevant to domains where data privacy, security, and trust are non-negotiable, including healthcare, biomedical research, and regulated AI deployments.

---

## Skills Demonstrated

- Federated Learning
- Privacy-Preserving Machine Learning
- Cybersecurity and Threat Modeling
- Hashing and Digital Signatures
- Trustworthy AI System Design
- Python-based implementation and experimentation

---


## Conclusion

This project showcases a secure, modular, and application-driven approach to Federated Learning in healthcare. It illustrates how AI systems can be designed to be both privacy-preserving and resilient to adversarial behavior, making it a strong candidate for academic, research, and scholarship-focused discussions.
