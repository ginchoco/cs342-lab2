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
    long_key = key * (len(str)/3)
    return xor(str, long_key)


def scoreText(str):
    count = 0
    for s in str:
        if s == 'e':
            count += 1
    return count

# find key with max score
def solveS1C03(s):
    # byte_dict = {}
    max_score = 0
    max_key = bytes([0])
    for i in range(0, 256):
        # convert int to byte
        # key = bytes([i])
        key_str = hex(i)

        # maybe convert key to string for caesarDecrypt?

        # byte_dict.add(key, scoreText(caesarDecrypt(s, key)))
        if scoreText(caesarDecrypt(s, key_str)) > max_score:
            max_score = scoreText(caesarDecrypt(s, key_str))
            max_key = key_str

    print(caesarDecrypt(s, max_key))
    return max_key
