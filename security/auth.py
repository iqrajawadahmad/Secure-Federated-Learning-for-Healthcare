from security.config import CLIENTS

def authenticate_client(client_id, token):
    if client_id not in CLIENTS:
        return False
    return CLIENTS[client_id] == token
