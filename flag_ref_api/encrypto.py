import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("USER_ENCRYPTION_KEY")

f = Fernet(key)


def encrypt(stuff: str):
    return str(f.encrypt(stuff.encode()).decode())


def decrypt(stuff: str):
    return str(f.decrypt(stuff.encode()).decode())
