import hashlib

def sha256_hash(text):
    # Encode string to bytes
    encoded_text = text.encode()
    # Create SHA-256 hash object
    hash_object = hashlib.sha256(encoded_text)
    # Return hexadecimal representation
    return hash_object.hexdigest()


data = input()
print("SHA-256:", sha256_hash(data))