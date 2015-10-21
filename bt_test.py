import unittest
from bt import *

class testBT(unittest.TestCase):

    def test_bt_to_int(self):
        self.assertEqual(bt_to_int('0'), 0)
        self.assertEqual(bt_to_int('N00'), -9)
        self.assertEqual(bt_to_int('N01'), -8)
        self.assertEqual(bt_to_int('N10'), -6)
        self.assertEqual(bt_to_int('NN'), -4)
        self.assertEqual(bt_to_int('N0'), -3)
        self.assertEqual(bt_to_int('N1'), -2)
        self.assertEqual(bt_to_int('11'), 4)
        self.assertEqual(bt_to_int('1N0'), 6)
        self.assertEqual(bt_to_int('100'), 9)
        self.assertRaises(Exception, bt_to_int, '3214')

    def test_int_to_bt(self):
        self.assertEqual(int_to_bt(0), '0')
        self.assertEqual(int_to_bt(-9), 'N00')
        self.assertEqual(int_to_bt(-8), 'N01')
        self.assertEqual(int_to_bt(-6), 'N10')
        self.assertEqual(int_to_bt(-4), 'NN')
        self.assertEqual(int_to_bt(-3), 'N0')
        self.assertEqual(int_to_bt(-2), 'N1')
        self.assertEqual(int_to_bt(4), '11')
        self.assertEqual(int_to_bt(6), '1N0')
        self.assertEqual(int_to_bt(9), '100')
        self.assertEqual(int_to_bt(3), '10')
        self.assertRaises(Exception, int_to_bt, 'N23')
        
    def test_add(self):
        store('0')
        self.assertEqual(memory, '0')
        add('N00')
        self.assertEqual(memory_as_int(), -9)
        add('100')
        self.assertEqual(memory_as_bt(), '0')
        add('1N')
        self.assertEqual(memory_as_int(), 2)      

    def test_subtract(self):
        store('100')
        subtract('1N1')
        self.assertEqual(memory_as_int(), 2)
        subtract('NN')
        self.assertEqual(memory_as_bt(), '1N0')

    def test_multipy(self):
        store('1')
        multiply('10N')
        self.assertEqual(memory_as_int(), 8)
        multiply('N')
        self.assertEqual(memory_as_bt(), 'N01')
        multiply('0')
        self.assertEqual(memory_as_int(), 0)

    def test_divide(self):
        store('10N')
        divide('11')
        self.assertEqual(memory_as_int(), 2)
        divide('N1')
        self.assertEqual(memory_as_bt(), 'N')
        divide('1NN')
        self.assertEqual(memory_as_bt(), '0')
        self.assertRaises(Exception, divide, '0')

    def test_remainder(self):
        store('N11')
        remainder('10')
        self.assertEqual(memory_as_bt(), '1')
        store('100')
        remainder('11')
        self.assertEqual(memory_as_int(), 1)
        store('100')
        remainder('1NN')
        self.assertEqual(memory_as_bt(), '11')
        self.assertRaises(Exception, remainder, '0')

    def test_negate(self):
        store('1N0')
        negate()
        self.assertEqual(memory_as_bt(), 'N10')
        store('N01')
        negate()
        self.assertEqual(memory_as_bt(), '10N')
        store('0')
        negate()
        self.assertEqual(memory_as_int(), 0)

    def test_store(self):
        store('N11')
        self.assertEqual(memory_as_bt(), 'N11')
        store('0')
        self.assertEqual(memory_as_int(), 0)
        store('100')
        self.assertEqual(memory_as_int(), 9)

    def test_memory_as_int(self):
        store('N11')
        self.assertEqual(memory_as_int(), -5)
        store('1N1')
        self.assertEqual(memory_as_int(), 7)
        store('0')
        self.assertEqual(memory_as_int(), 0)

    def test_memory_as_bt(self):
        store('N11')
        self.assertEqual(memory_as_bt(), 'N11')
        store('1N1')
        self.assertEqual(memory_as_bt(), '1N1')
        store('0')
        self.assertEqual(memory_as_bt(), '0')

    def test_evaluate(self):
        self.assertEqual(evaluate('=1NN1 +N01 *1N'), '1NN1')
        self.assertEqual(evaluate('= N00- N0 / N1'), '10')
        self.assertEqual(evaluate('=   1N0 /   N10 *NN % 10'), '1')

unittest.main()
