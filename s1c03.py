'''
From this point on, I'm not providing the number of arguments.
Part of your job is to understand the contracts of these methods
and how they fit together.
'''
from s1c02 import xor

def caesarEncrypt(str, key):
    long_key = key * len(str)
    return xor(str, long_key)


def caesarDecrypt(str, key):
    long_key = key * len(str)
    # print("str" + str)
    print("key" + key)
    return xor(str, long_key) #xor takes in 2 bytes to XOR


def scoreText(str):
    count = 0
    # dict = {"ETAOIN SHRDLU"}
    s = str.decode()
    for b in s:
        if s in "ETAOIN SHRDLU etaoin shrdlu":
            count += 1
        elif s < 'A' or s > 'z':
            count -=10
    return count

# find key with max score
def solveS1C03(s):
    # byte_dict = {}
    max_score = 0
    max_key = bytes([0])
    for i in range(0, 256):
        # convert int to byte
        key = bytes([i])
        # key_str = (i)

        # byte_dict.add(key, scoreText(caesarDecrypt(s, key)))
        if scoreText(caesarDecrypt(s, key)) > max_score:
            max_score = scoreText(caesarDecrypt(s, key))
            max_key = key

    print(caesarDecrypt(s, max_key))
    return max_key
