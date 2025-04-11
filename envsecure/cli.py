import click
from .encryptor import encrypt_env_file, decrypt_env_file
from .utils import generate_key_file

@click.group()
def cli():
    pass

@cli.command()
@click.option('--output', default='secret.key', help='Output key file path')
def keygen(output):
    """Generate a new AES-256 key file."""
    generate_key_file(output)

@cli.command()
@click.option('--key', required=True, help='Path to AES key file')
@click.option('--env', required=True, help='Path to .env file to encrypt')
@click.option('--output', default=None, help='Encrypted output file path')
def encrypt(key, env, output):
    """Encrypt a .env file using AES-256."""
    encrypt_env_file(env, key, output)

@cli.command()
@click.option('--key', required=True, help='Path to AES key file')
@click.option('--env', required=True, help='Encrypted .env file path')
@click.option('--output', default=None, help='Decrypted output file path')
def decrypt(key, env, output):
    """Decrypt an encrypted .env file."""
    decrypt_env_file(env, key, output)
