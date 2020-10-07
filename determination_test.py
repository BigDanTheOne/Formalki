import unittest

from Determination import determine

alphabet = ["a", "b", "c"]
NKA = [[(1, "c"), (2, "a")],
       [(1, "b")],
       [(1, "c"), (3, "c")],
       [(3, "c")]]
DKA = {"0": [("2", "a"), ("1", "c")],
               "1": [("1", "b")],
               "2": [("1#3", "c")],
               "1#3": [("1", "b"), ("3", "c")],
               "3": [("3", "c")]}
nka_final_states = {"1", "3"}
dka_final_states = {"1", "3", "1#3"}


class MyTest(unittest.TestCase):
    global alphabet, NKA, DKA

    def doTest(self):
        self.assertEqual(determine(alphabet, NKA, nka_final_states)[0], DKA)
        self.assertEqual(determine(alphabet, NKA, nka_final_states)[1], dka_final_states)


if __name__ == '__main__':
    unittest.main()