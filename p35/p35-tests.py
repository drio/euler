import unittest

from p35 import is_circular_prime, enum_circular, shift

class TestLogic(unittest.TestCase):
    def test_shift(self):
        self.assertEqual(shift(123), 312)
        self.assertEqual(shift(12), 21)
        self.assertEqual(shift(1), 1)
        self.assertEqual(shift(None), None)

    def test_enum_circular(self):
        cir = enum_circular(12)
        self.assertEqual(len(cir), 2)
        self.assertEqual(12 in cir, True)
        self.assertEqual(21 in cir, True)

        cir = enum_circular(123)
        self.assertEqual(len(cir), 3)
        self.assertEqual(123 in cir, True)
        self.assertEqual(312 in cir, True)
        self.assertEqual(231 in cir, True)

    def test_circular_prime(self):
        primes = set([21, 12])
        self.assertEqual(is_circular_prime(12, primes), True)

if __name__ == '__main__':
    unittest.main()
