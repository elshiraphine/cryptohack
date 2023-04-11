from pwn import * # pip install pwntools
import json
from Crypto.Util.number import *
import base64

def rot13solver(message):
    res = ""

    for char in message:
        if (char.isalpha()):
            if (char.isupper()):
                res += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                res += chr((ord(char) - 97 + 13) % 26 + 97) 
        else:
            res += char
    return res

def utf8solver (message):
    res = ""
    for char in message:
        res += chr(char)

    return res

def bigintsolver (message):
    if message[:2] == "0x" :
        bytestr = bytes.fromhex(message[2:])
    else:
        bytestr = message
    res = bytestr.decode("utf-8")
    return res

def decode():
    payload = received["encoded"]

    if (received["type"] == "rot13"):
        to_send = {
            "decoded": rot13solver(payload)
        }

    elif (received["type"] == "utf-8"):
        to_send = {
            "decoded": utf8solver(payload)
        }
    
    elif (received["type"] == "hex"):
        to_send = {
            "decoded": bytes.fromhex(payload).decode()
        }
    
    elif (received["type"] == "bigint"):
        payload = received["encoded"]
        to_send = {
            "decoded": bigintsolver(payload)
        }

    elif (received["type"] == "base64"):
        payload = received["encoded"]
        to_send = {
            "decoded": base64.b64decode(payload).decode()
        }
    return to_send


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    to_send = decode()

    json_send(to_send)
    