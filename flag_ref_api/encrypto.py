import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("USER_ENCRYPTION_KEY")

f = Fernet(key)


def encrypt(stuff: str):
    return f.encrypt(stuff.encode())


def decrypt(stuff: str):
    return f.decrypt(stuff)
