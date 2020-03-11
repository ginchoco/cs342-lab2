from s1c03 import *
import sys
import binascii as b
#from s1c02 import xor

def solveS1C04(fileStr):
    f = open(fileStr, 'r')
    if f.mode == 'r':
        contents = f.readlines()

        top_score = 0
        pt = ""
        for x in contents:
            bytes_input = b.unhexlify(x.strip())
            key = solveS1C03(bytes_input)
            plaintext = caesarDecrypt(bytes_input, key)
            current_score = scoreText(plaintext)
            if current_score > top_score:
                top_score = current_score
                pt = plaintext
        f.close()

        return pt.strip()
