import binascii as b

def b64ToHex(b64String):
    # given binary, produce hex.
    return b.hexlify(b.a2b_base64(b64String))


def hexToB64(hexString):
    return b.b2a_base64(b.unhexlify(hexString), newline=False)
    # removes newline
