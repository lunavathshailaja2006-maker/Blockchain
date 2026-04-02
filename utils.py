import hashlib

def create_hash(data: str) -> str:
"""
Generate SHA-256 hash of the given data
"""
return hashlib.sha256(data.encode()).hexdigest()
