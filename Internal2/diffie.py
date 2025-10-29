def is_primitive_root(g, p):
    # Check if g is a primitive root of prime p
    required_set = {num for num in range(1, p)}
    actual_set = {pow(g, powers, p) for powers in range(1, p)}
    return required_set == actual_set


def find_primitive_root(p):
    # Try every number from 2 to p-1
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None


# --- Diffie-Hellman Key Exchange ---
def diffie_hellman(p, a, b):
    # Step 1: find primitive root
    g = find_primitive_root(p)

    print("Publicly shared values:")
    print("Prime (p):", p)
    print("Primitive root (g):", g)

    # Step 2: compute public keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    print("\nPublic keys exchanged:")
    print("Alice's public key (A):", A)
    print("Bob's public key (B):", B)

    # Step 3: compute shared secrets
    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)

    print("\nShared secrets computed:")
    print("Alice's secret:", alice_secret)
    print("Bob's secret:", bob_secret)

    if alice_secret == bob_secret:
        print("\n✅ Shared secret established successfully!")
    else:
        print("\n❌ Error: Shared secrets do not match.")

# --- Example Run ---
p = int(input())        # prime number
a = int(input())          # Alice's private key
b = int(input())        # Bob's private key

diffie_hellman(p, a, b)