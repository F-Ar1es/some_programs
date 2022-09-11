from hmac import digest
from inspect import signature
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA384
from Crypto.PublicKey import RSA
import base64
import hashlib


active_key = input("Input machine code: ")
pri_key = RSA.import_key(open("./pri_key.pem", mode="r").read())

digest = SHA384.new(active_key.encode('utf-8'))
signature = pkcs1_15.new(pri_key).sign(digest)
key_send = base64.b64encode(signature)

print(key_send)