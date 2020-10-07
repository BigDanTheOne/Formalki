import unittest

from MakingComplite import makeComplete

alphabet = ["a", "b", "c"]
DKA = {"0": [("2", "a"), ("1", "c")],
               "1": [("1", "b")],
               "2": [("1#3", "c")],
               "1#3": [("1", "b"), ("3", "c")],
               "3": [("3", "c")]}
PDKA = {"0": [("2", "a"), ("1", "c"), ("5", "b")],
                "1": [("1", "b"), ("5", "a"), ("5", "c")],
                "2": [("1#3", "c"), ("5", "a"), ("5", "b")],
                "1#3": [("1", "b"), ("3", "c"), ("5", "a")],
                "3": [("3", "c"), ("5", "a"), ("5", "b")],
                "5": [("5", "a"), ("5", "b"), ("5", "c")]}
dka_final_states = {"1", "3", "1#3"}


class MyTest(unittest.TestCase):
    global alphabet,  DKA

    def doTest(self):
        self.assertEqual(makeComplete(DKA, alphabet), PDKA)


if __name__ == '__main__':
    unittest.main()