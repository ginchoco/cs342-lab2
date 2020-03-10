'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''
from s1c02 import xor

def caesarEncrypt(s, key):
    long_key = key * len(s)
    return xor(s, long_key)


def caesarDecrypt(s, key):
    long_key = key * len(s)
    return xor(s, long_key) #xor takes in 2 bytes to XOR


def scoreText(byte_input): #inputs bytes
    count = 0
    
    try: # try to decode the byte_input
        s = byte_input.decode() #convert to string
        for b in s:
            if b in "ETAOIN SHRDLU etaoin shrdlu":
                count += 1
            elif b < 'A' or s > 'z':
                count -=10
        return count
    except: # if it's an unprintable byte_input then it's not english text
        return -1


# find key with max score
def solveS1C03(s): #input bytes, unhexlify(string)
    max_score = 0
    max_key = bytes([0]) #initial key
    for i in range(0, 256):
        # convert int to byte
        key = bytes([i]) #create byte objects for each int
        this_score = scoreText(caesarDecrypt(s, key))
        if this_score > max_score:
            max_score = this_score
            max_key = key

    # print(caesarDecrypt(s, max_key))
    return max_key 
