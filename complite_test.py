import unittest

from Complition import makeComplete

alphabet = ["a", "b", "c"]
DKA = {"0": [("1", "a"), ("2", "b"), ("3", "c")],
       "1": [("2", "b")],
       "2": [("0#1", "a")],
       "3": [("1#2", "b"), ("3", "c")],
       "0#1": [("1", "a"), ("2", "b"), ("3", "c")],
       "1#2": [("0#1", "a"), ("2", "b")]}
PDKA = {'0': [('1', 'a'), ('2', 'b'), ('3', 'c')],
        '1': [('2', 'b'), ('6', 'a'), ('6', 'c')],
        '2': [('0#1', 'a'), ('6', 'b'), ('6', 'c')],
        '3': [('1#2', 'b'), ('3', 'c'), ('6', 'a')],
        '0#1': [('1', 'a'), ('2', 'b'), ('3', 'c')],
        '1#2': [('0#1', 'a'), ('2', 'b'), ('6', 'c')],
        '6': [('6', 'a'), ('6', 'b'), ('6', 'c')]}

class MyTest(unittest.TestCase):
    global alphabet,  DKA

    def doTest(self):
        self.assertEqual(makeComplete(DKA, alphabet), PDKA)


if __name__ == '__main__':
    unittest.main()