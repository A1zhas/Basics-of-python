import unittest
import math

class TestBuiltInFunctions(unittest.TestCase):
    
    def test_filter(self):
        self.assertEqual(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])), [2, 4])
        self.assertEqual(list(filter(None, ["", "Hello", "World", None])), ["Hello", "World"])
        self.assertEqual(list(filter(lambda x: x > 0, [])), [])

    def test_map(self):
        self.assertEqual(list(map(lambda x: x**2, [1, 2, 3])), [1, 4, 9])
        self.assertEqual(list(map(str.upper, ["hello", "world"])), ["HELLO", "WORLD"])
        self.assertEqual(list(map(lambda x: x + 1, [])), [])

    def test_sorted(self):
        self.assertEqual(sorted([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sorted(["banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
        self.assertEqual(sorted([1]), [1])

class TestMathFunctions(unittest.TestCase):

    def test_pi(self):
        self.assertAlmostEqual(math.pi, 3.14159, places=5)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)
        self.assertEqual(math.sqrt(0), 0)
        with self.assertRaises(ValueError):
            math.sqrt(-1)

    def test_pow(self):
        self.assertEqual(math.pow(2, 3), 8)
        self.assertEqual(math.pow(2, -1), 0.5)
        self.assertEqual(math.pow(2, 0), 1)

    def test_hypot(self):
        self.assertEqual(math.hypot(3, 4), 5)
        self.assertEqual(math.hypot(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
