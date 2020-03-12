# import binascii as b
from s1c02 import xor
import sys


# We want to find the length of our key, this can be any value from 2 to ~40 characters
# Compute the difference in bits between two strings
def editDistance(k1, k2):
    # xor the two byte strings
    #print(len(k1))
    #print(len(k2))
    if (len(k1)) != (len(k2)):
        print(-1)
        return -1
    res = xor(k1, k2)
    # convert to integer
    n = int.from_bytes(res, byteorder='big', signed=False)
    # return count of occurences of 1 bits
    #print(n)
    # print(type(n))
    return bin(n).count("1")

# test
# s.editDistance(b"this is a test", b"wokka wokka!!!")


# def findEditDist(bytestr1, bytestr2):e
def getKeySize(input):
    min_avg = 9000000
    min_keysize = 0
    # len(input)//3
    for i in range(1,20):
        print(str(i))
        slice1 = input[0:i]
        slice2 = input[i:(2*i)]
        slice3 = input[(2*i) : (3*i)]
        slice4 = input[(3*i) : (4*i)]
        edit1 = editDistance(slice1, slice2)/i
        edit2 = editDistance(slice2, slice3)/i
        edit3 = editDistance(slice3, slice4)/i
        edit4 = editDistance(slice1, slice3)/i
        edit5 = editDistance(slice1, slice4)/i
        edit6 = editDistance(slice2, slice4)/i
        avg = (edit1 + edit2 + edit3 + edit4 + edit5 + edit6)/6
        # avg = edit1
        print(avg)
        if avg < min_avg:
            min_avg = avg
            min_keysize = i

    return min_keysize


def solveS1C06():
    pass
