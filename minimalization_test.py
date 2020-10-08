import unittest
from Minimization import minimize

PDKA = {'0': [('1', 'a'), ('2', 'b'), ('3', 'c')],
        '1': [('2', 'b'), ('6', 'a'), ('6', 'c')],
        '2': [('0#1', 'a'), ('6', 'b'), ('6', 'c')],
        '3': [('1#2', 'b'), ('3', 'c'), ('6', 'a')],
        '0#1': [('1', 'a'), ('2', 'b'), ('3', 'c')],
        '1#2': [('0#1', 'a'), ('2', 'b'), ('6', 'c')],
        '6': [('6', 'a'), ('6', 'b'), ('6', 'c')]}

final_states = {'0#1', '1#2', '2', '1'}

alphabet = ["a", "b", "c"]

classes = {'0': 0, '1': 1, '2': 2, '3': 3, '0#1': 4, '1#2': 5, '6': 6}


class MyTest(unittest.TestCase):
    def doTest(self):
        self.assertEqual(minimize(PDKA, alphabet, final_states), classes)


#if __name__ == '__main__':
unittest.main()
