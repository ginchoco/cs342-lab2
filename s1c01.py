import binascii as b

def b64ToHex(b64String):
    binary_rep = b.a2b_base64(b64String)
    return b.hexlify(binary_rep)

def hexToB64(hexString):
    pass

print(b64ToHex('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'))