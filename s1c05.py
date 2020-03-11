from s1c02 import xor


def vigenereEncrypt(str):

    # Extend ICE to the length of the input
    key = b"ICE"
    key_multiples = (len(str)//3) + 1
    key = key * key_multiples
    key = key[0:(len(str))] # shorten to correct length
    # XOR the long key with str
    return xor(key, str)

def vigenereDecrypt(str):
    return vigenereEncrypt(str)
