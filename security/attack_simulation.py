import numpy as np

def malicious_update(shape):
    return [np.random.uniform(-10, 10, size=w.shape) for w in shape]
