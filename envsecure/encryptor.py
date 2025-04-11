import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

BLOCK_SIZE = 16

def pad(data):
    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + (chr(padding) * padding).encode()

def unpad(data):
    padding = data[-1]
    return data[:-padding]

def encrypt_env_file(env_path, key_path, output_path=None):
    with open(env_path, 'rb') as f:
        plaintext = f.read()

    with open(key_path, 'rb') as f:
        key = f.read()

    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext))

    result = b64encode(iv + ciphertext).decode()
    output_path = output_path or (env_path + '.enc')
    with open(output_path, 'w') as f:
        f.write(result)

    print(f"Encrypted and saved to {output_path}")

def decrypt_env_file(enc_path, key_path, output_path=None):
    with open(enc_path, 'r') as f:
        encrypted = b64decode(f.read())

    with open(key_path, 'rb') as f:
        key = f.read()

    iv = encrypted[:BLOCK_SIZE]
    ciphertext = encrypted[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))

    output_path = output_path or enc_path.replace('.enc', '')
    with open(output_path, 'wb') as f:
        f.write(plaintext)

    print(f"Decrypted and saved to {output_path}")
