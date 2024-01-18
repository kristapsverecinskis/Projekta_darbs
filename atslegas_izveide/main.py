from cryptography.fernet import Fernet

KEY_FILE = 'parole.key'
atsl = Fernet.generate_key()

with open(KEY_FILE, 'wb') as atslega:
    atslega.write(atsl)

