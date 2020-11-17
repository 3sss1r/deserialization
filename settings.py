import hmac
import hashlib


SECRET_TOKEN = b'secret_pickle_token'


def check_hash(message, digest_mod=hashlib.sha256, secret_token=SECRET_TOKEN):
    return hmac.new(secret_token, message, digest_mod).digest()
