import unittest


class TestTaxAmount(unittest.TestCase):
    def test_amount1(self):
        self.assertEqual(taxamount(999, 3), 0)
        self.assertEqual(taxamount(1001, 3), 600.6)
        self.assertEqual(taxamount(3001, 3), 3601.2)


if __name__ == '__main__':
    unittest.main()
