## Encoding Challenge 40pts

In this challenge we were given some python file, first to create a connection with the server, and the second was a file that would make it easier to answer the challenge because it contains methods for encoding messages.

There are five type encoding, and here is my approach:
1. rot13

    The payload of this encoding type was a string that encoded with rot13.
    ```py
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
    ```

2. utf-8

    The payload of this message was a list that containing integer number, so we need a `chr()` function to decode it into utf-8 format.
    ```py
    def utf8solver (message):
    res = ""
    for char in message:
        res += chr(char)

    return res
    ```

3. hex

    The payload of this message was a hex so we only need a bult-in `bytes.fromhex()` functions, and convert the bytes object to string using `decode()`.
    ```py
    bytes.fromhex(payload).decode()
    ```

4. base64

    The payload of this message wase a base64 string so we need to import `base64` and use the `b64decode()` To convert the bytes objcet to string we need to use `decode()`
    ```py
    base64.b64decode(payload).decode()
    ``` 

5. bigint

    The payload of this message was a hex, but we need to specify that the payload containing `0x` or not.
    ```py
    def bigintsolver (message):
    if message[:2] == "0x" :
        bytestr = bytes.fromhex(message[2:])
    else:
        bytestr = message
    res = bytestr.decode("utf-8")
    return res
    ```

To get the full code you can get it [here](solver.py).