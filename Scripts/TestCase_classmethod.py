import unittest

class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("this is login test")

    @classmethod
    def tearDown(self):
        print("this is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close application")

    def test_search(self):
        print("This is a search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")
