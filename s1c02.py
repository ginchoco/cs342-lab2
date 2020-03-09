import binascii as b

def xor(s1, s2):
    # convert s1 and s2 from byte strings to binary
    # s1b = bytearray.fromhex(s1)
    # print(s2)
    # s2b = bytearray.fromhex(s2)

    # perform XOR, iterating one byte at a time
    res_arr = []

    for i in range(len(s1)):
        res_arr.append(s1[i] ^ s2[i])

    # convert result back to byte strings
    # print(bytes(res_arr))
    return bytes(res_arr) #creates a byte object from the array

#s1c02.xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
#should input and output types be strings or byte strings?
