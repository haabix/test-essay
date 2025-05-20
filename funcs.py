import hashlib

def hashstring(string: str):
    return hashlib.sha256(string.encode()).hexdigest()