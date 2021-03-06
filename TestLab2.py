import unittest
import binascii

from s1c01 import b64ToHex, hexToB64
from s1c02 import xor
from s1c03 import solveS1C03, caesarEncrypt, caesarDecrypt, scoreText
from s1c04 import solveS1C04
from s1c05 import vigenereEncrypt, vigenereDecrypt
from s1c06 import editDistance, getKeySize, solveS1C06
from s1c07 import AES_ECB_encrypt, AES_ECB_decrypt
from s1c08 import solveS1C08

class TestLab2(unittest.TestCase):

    '''Here's an example of what some test cases might look like.'''

    def test_s1c01_hexToB64(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(hexToB64(hexString), b64String)


    '''One more example.'''

    def test_s1c01_b64ToHex(self):
        testCases = [
            (
                b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d',
                b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
            ),
            (b'4e6f6e204d696e6973747261726920736564204d696e69737472617265', b'Tm9uIE1pbmlzdHJhcmkgc2VkIE1pbmlzdHJhcmU='),
            (b'', b''),
            (b'61', b'YQ=='),
            (b'6666666664643435', b'ZmZmZmRkNDU=')

        ]
        for hexString, b64String in testCases:
            self.assertEqual(b64ToHex(b64String), hexString)

    # @unittest.skip('Not yet implemented')
    def test_s1c02_xor(self):
        '''
        Starting here, write your own tests. You can generate tests in a variety
        of ways, ranging from trivial tests (does the empty string produce the empty
        string?) to tests of properties (does xor preserve length?) to tests of types
        (is the return type of this method correct?) to specific cases (is the xor
        of these two specific byte strings equal to the correct byte string?).

        To generate specific cases, I'd suggest either using very small examples
        you can work by hand, or generate the test cases using other code you write
        or online calculators.
        '''
        testCases = [
            ("1c0111001f010100061a024b53535009181c",
            "686974207468652062756c6c277320657965",
            "746865206b696420646f6e277420706c6179") #expected_res
            ]

        for str1, str2, expected_res in testCases: # call unhexlify on strings converted to bytes
            self.assertEqual(xor(binascii.unhexlify(str1), binascii.unhexlify(str2)), binascii.unhexlify(expected_res))

    # @unittest.skip('Not yet implemented')
    def test_s1c03_caesarEncrypt(self):
        testCases = [
        (b"Cooking MC's like a pound of bacon", b'X', "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")]
        for plaintext, k, ciphertext in testCases:
            self.assertEqual(caesarEncrypt(plaintext, k), binascii.unhexlify(ciphertext))

    # @unittest.skip('Not yet implemented')
    def test_s1c03_caesarDecrypt(self):
        testCases = [("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", b'X')]
        for encrypted, k in testCases:
            self.assertEqual(solveS1C03(binascii.unhexlify(encrypted)), k)
        # s.solveS1C03(bin.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))


    # @unittest.skip('Not yet implemented')
    def test_s1c03_scoreText(self):
        testCases = [
        (b"ETAOIN SHRDLU etaoin shrdlu", len("ETAOIN SHRDLU etaoin shrdlu"))
        ]
        for t, count in testCases:
            self.assertEqual(scoreText(t), count)


    '''
       ********
       Remember! You can and should add more test methods to this file to test
       other helper methods that you write in the course of this lab.
       ********
    '''

    '''
    @unittest.skip('Not yet implemented')
    def test_s1c03_solveS1C3(self):

        You might find that it's less clear what the testable contract of the methods
        that just solve the challenges is. If you choose, you can decide not to use
        this test method, and instead just test the helper methods you write to make
        solveSXCY() methods work.

        self.assertEqual(True, False)

    '''

    #@unittest.skip('Not yet implemented')
    def test_s1c04_solveS1C4(self):
        testCases = [("set1ch4.txt", b'Now that the party is jumping')]
        for filename, ans in testCases:
            self.assertEqual(solveS1C04(filename), ans)

    # @unittest.skip('Not yet implemented')
    def test_s1c05_vigenereEncrypt(self):
        testCases = [(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal",
        b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')
        ]
        for testStr, res in testCases:
            self.assertEqual(binascii.hexlify(vigenereEncrypt(testStr)), res)

    # @unittest.skip('Not yet implemented/')
    def test_s1c05_vigenereDecrypt(self):
        testCases = [(b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f',
        b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
        ]
        for testBytes, res in testCases:
            self.assertEqual(vigenereDecrypt(binascii.unedhexlify(testBytes)), res)

    @unittest.skip('Not yet implemented')
    def test_s1c06_editDistance(self):
        testCases = [ (b"this is a test", b"wokka wokka!!!", 37)

        ]
        for s1, s2, dist in testCases:
            self.assertEqual(editDistance(s1, s2), dist)


    def test_s1c06_getKeySize(self):
        testCases = [(b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f',
        3)]
        for testStr, res in testCases:
            self.assertEqual(getKeySize(testStr), res)

    @unittest.skip('Not yet implemented')
    def test_s1c06_solveS1C6(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_encrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c07_AES_ECB_decrypt(self):
        self.assertEqual(True, False)

    @unittest.skip('Not yet implemented')
    def test_s1c08_solveS1C8(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
