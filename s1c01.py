import binascii

def b64ToHex(b64String):
    pass

def hexToB64(hexString):
    return binascii.hexlify(binascii.a2b_base64(hexString))
