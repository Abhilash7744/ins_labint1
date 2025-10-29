import random
import hashlib
from math import gcd

# Fast modular exponentiation
def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

# Extended Euclidean Algorithm for modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Hash message to integer
def hash_message(message):
    h = hashlib.sha256(message.encode()).hexdigest()
    return int(h, 16)

# -------------------- Key Generation --------------------
def generate_keys():
    q = 23      # A prime number
    a = 2          # Generator
    XA = random.randint(1, q-2)    # Private key
    YA = mod_pow(a, XA, q)          # Public key
    return (q, a, YA), XA

# -------------------- Signing --------------------
def sign(message, q, a, XA):
    H = hash_message(message)
    while True:
        k = random.randint(1, q-2)
        if gcd(k, q-1) == 1:
            break
    s1 = mod_pow(a, k, q)
    k_inv = mod_inverse(k, q-1)
    s2= (k_inv * (H - XA * s1))
    return (s1, s2)

# -------------------- Verification --------------------
def verify(message, signature, q, a, YA):
    s1, s2 = signature
    H = hash_message(message)
    left = mod_pow(a, H, q)
    right = (mod_pow(YA, s1, q) * mod_pow(s1, s2, q)) % q
    return left == right

# -------------------- Demo --------------------
public_key, private_key = generate_keys()
p, g, y = public_key

message = input()
signature = sign(message, p, g, private_key)

print("Message:", message)
print("Signature:", signature)
print("Verification:", verify(message, signature, p, g, y))
print("Verification (tampered):", verify("Hi ElGamal!", signature, p, g, y))