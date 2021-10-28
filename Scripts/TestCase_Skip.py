import unittest

class AppTesting(unittest.TestCase):

    @unittest.skip
    def test_search(self):
        print("This is a search test")

    @unittest.skipIf(1 == 1, "Numbers are equal")
    def test_advancedSearch(self):
        print("This is an advanced search test")

    @unittest.skip("Skipping test - it is not ready")
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

if __name__ == "__main__":
    unittest.main
