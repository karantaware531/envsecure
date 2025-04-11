'''
# envsecure

A secure CLI tool to encrypt/decrypt .env files for safe deployment in CI/CD pipelines.

## Installation
```bash
pip install envsecure  # after upload to PyPI
```

## Usage
```bash
# Generate key
envsecure keygen --output secret.key

# Encrypt a .env file
envsecure encrypt --key secret.key --env /path/to/.env

# Decrypt the file
envsecure decrypt --key secret.key --env /path/to/.env.enc
```

## License
MIT
'''
