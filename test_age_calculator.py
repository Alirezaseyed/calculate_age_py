import unittest
import datetime

class TestAgeCalculator(unittest.TestCase):
    def test_calculate_age_valid(self):
        self.assertEqual(calculate_age(1990), datetime.datetime.now().year - 1990)

    def test_calculate_age_future(self):
        with self.assertRaises(ValueError):
            calculate_age(datetime.datetime.now().year + 1)

    def test_calculate_age_negative(self):
        with self.assertRaises(ValueError):
            calculate_age(-100)

    def test_calculate_age_zero(self):
        with self.assertRaises(ValueError):
            calculate_age(0)

if __name__ == "__main__":
    unittest.main()