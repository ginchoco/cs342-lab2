import binascii as b

def xor(s1, s2):
    # convert s1 and s2 from byte strings to binary
    s1b = bytearray.fromhex(s1)
    s2b = bytearray.fromhex(s2)

    # perform XOR, iterating one byte at a time
    res_arr = []

    for i in range(len(s1b)):
        res_arr.append(s1b[i] ^ s2b[i])

    # convert result back to byte strings
    return bytes(res_arr).hex()

#s1c02.xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
#should input and output types be strings or byte strings?
