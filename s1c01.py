import binascii

def b64ToHex(b64String):
    binary_rep = b.a2b_base64(b64String)
    return b.hexlify(binary_rep)

def hexToB64(hexString):
    return binascii.hexlify(binascii.a2b_base64(hexString))
