def row_transpose_encrypt(plaintext, key):
    # key: list of column orders, e.g. [3,1,4,2]
    key_order = key
    cols = len(key_order)
    rows = (len(plaintext) + cols - 1) // cols
    grid = [['X']*cols for _ in range(rows)]
    it = iter(plaintext)
    for r in range(rows):
        for c in range(cols):
            try:
                grid[r][c] = next(it)
            except StopIteration:
                grid[r][c] = 'X'
    # read by columns in order of key
    out = []
    for k in sorted(range(cols), key=lambda i: key_order[i]):
        for r in range(rows):
            out.append(grid[r][k])
    return ''.join(out)

def row_transpose_decrypt(ciphertext, key):
    cols = len(key)
    rows = (len(ciphertext) + cols - 1) // cols
    grid = [['']*cols for _ in range(rows)]
    # determine column lengths (all rows full here because padding used)
    idx = 0
    for k in sorted(range(cols), key=lambda i: key[i]):
        for r in range(rows):
            grid[r][k] = ciphertext[idx]; idx += 1
    return ''.join(grid[r][c] for r in range(rows) for c in range(cols)).rstrip('X')

# example
if __name__ == "__main__":
    k = [3,1,4,2]  # numeric key per column index
    pt = "THISISASECRETMESSAGE"
    ct = row_transpose_encrypt(pt, k)
    print(ct)
    print(row_transpose_decrypt(ct, k))
