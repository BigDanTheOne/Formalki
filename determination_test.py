import unittest

from Determination import determine

alphabet = ["a", "b", "c"]
NKA = [[(1, "a"), (2, "b"), (3, "c")],
       [(2, "b")],
       [(0, "a"), (1, "a")],
       [(2, "b"), (1, "b"), (3, "c")]]
DKA = {"0": [("1", "a"), ("2", "b"), ("3", "c")],
       "1": [("2", "b")],
       "2": [("0#1", "a")],
       "3": [("1#2", "b"), ("3", "c")],
       "0#1": [("1", "a"), ("2", "b"), ("3", "c")],
       "1#2": [("0#1", "a"), ("2", "b")]}
nka_final_states = {"1", "2"}
dka_final_states = {"1", "2", "0#1", "1#2"}


class MyTest(unittest.TestCase):
    global alphabet, NKA, DKA

    def doTest(self):
        self.assertEqual(determine(alphabet, NKA, nka_final_states)[0], DKA)
        self.assertEqual(determine(alphabet, NKA, nka_final_states)[1], dka_final_states)


if __name__ == '__main__':
    unittest.main()