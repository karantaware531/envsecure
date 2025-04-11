from Crypto.Random import get_random_bytes

def generate_key_file(path):
    key = get_random_bytes(32)
    with open(path, 'wb') as f:
        f.write(key)
    print(f"Key saved to {path}")
