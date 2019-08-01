import unittest

import cryptoskulls.colors.functions

class CryptoskullsColorsFunctionTest(unittest.TestCase):

    def test_split_rgb(self):
        test_cases = [
            ('#FFFFFFFF', (0xFF, 0xFF, 0xFF, 0xFF)),
            ('#AABBCCDD', (0xAA, 0xBB, 0xCC, 0xDD)),
            ('#AABBCC', (0xAA, 0xBB, 0xCC, 0xFF)),
        ]
        for test_case in test_cases:
            actual = cryptoskulls.colors.functions.split_rgba(test_case[0])
            self.assertTrue(
                actual == test_case[1],
                "Expected %s but got %s" % (test_case[1], actual)
            )
