import unittest


def taxamount(income, no_of_months):
    if isinstance(income, str) or isinstance(no_of_months, str):
        raise ValueError("String values are not allowed for income or number of months.")

    if not isinstance(income, (int, float)) or not isinstance(no_of_months, (int, float)):
        raise ValueError("Both income and number of months must be numeric types (int or float).")

    if income <= 0 or no_of_months <= 0:
        raise ValueError("Both income and number of months must be positive numbers.")

    if income < 1000:
        return 0.0
    elif income < 3000:
        return round(income * 0.2 * no_of_months, 1)
    else:
        return round(income * 0.4 * no_of_months, 1)


# print(taxamount(5000, 3))  # should return 6000.0

class TestTaxAmount(unittest.TestCase):
    def test_amount1(self):
        self.assertEqual(taxamount(999.9, 3), 0.0)
        self.assertEqual(taxamount(2500, 3), 1500.0)
        self.assertEqual(taxamount(4500, 3), 5400.0)


if __name__ == '__main__':
    unittest.main()
