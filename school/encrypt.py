import base64
import random

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def get_encrypt_str_from_js(pwd: str, pwdEncryptSalt: str) -> str:
    """
    从js中获取加密字符串
    """
    import execjs

    with open("encrypt.js", "r", encoding="utf-8") as f:
        js = f.read()
    ctx = execjs.compile(js)
    return ctx.call("encryptAES", pwd, pwdEncryptSalt)


def get_random_string(length: int) -> str:
    """
    获取随机字符串
    """

    return "".join(
        random.choices("ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678", k=length)
    )


def encrypt_aes(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext


def get_aes_string(n: str, f: str, c: str) -> str:
    """
    获取加密字符串
    """
    f = f.replace(r"/(^\s+)|(\s+$)/g", "")
    f_bytes = f.encode("utf-8")
    c_bytes = c.encode("utf-8")
    encrypt_bytes = encrypt_aes(f_bytes, c_bytes, n.encode("utf-8"))
    return base64.b64encode(encrypt_bytes).decode("utf-8")


def get_encrypt_str(pwd: str, pwdEncryptSalt: str) -> str:
    """
    获取加密字符串
    """
    n = get_random_string(64) + pwd
    f = pwdEncryptSalt
    c = get_random_string(16)
    return get_aes_string(n, f, c)
