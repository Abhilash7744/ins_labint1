from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_cbc(plaintext_bytes, key_bytes):
    # key_bytes must be 16, 24, or 32 bytes
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext_bytes, AES.block_size))
    return iv + ct

def aes_decrypt_cbc(iv_ct, key_bytes):
    iv = iv_ct[:16]
    ct = iv_ct[16:]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size)

# example
if __name__ == "__main__":
    key = get_random_bytes(32)  # AES-256
    pt = b"Top secret message for AES"
    ct = aes_encrypt_cbc(pt, key)
    print("cipher (hex):", ct.hex())
    print("decrypted:", aes_decrypt_cbc(ct, key))
