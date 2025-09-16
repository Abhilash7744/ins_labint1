def rail_fence_encrypt(text, rails):
    if rails <= 1: return text
    fence = [''] * rails
    rail = 0
    direction = 1
    for ch in text:
        fence[rail] += ch
        rail += direction
        if rail == 0 or rail == rails-1: direction *= -1
    return ''.join(fence)

def rail_fence_decrypt(cipher, rails):
    if rails <= 1: return cipher
    n = len(cipher)
    pattern = []
    rail = 0
    direction = 1
    for _ in range(n):
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == rails-1: direction *= -1
    counts = [pattern.count(r) for r in range(rails)]
    parts = []
    idx = 0
    for c in counts:
        parts.append(cipher[idx:idx+c])
        idx += c
    pointers = [0]*rails
    result = []
    for r in pattern:
        result.append(parts[r][pointers[r]])
        pointers[r] += 1
    return ''.join(result)

# example
if __name__ == "__main__":
    ct = rail_fence_encrypt("WEAREDISCOVEREDFLEEATONCE", 3)
    print(ct)
    print(rail_fence_decrypt(ct, 3))
