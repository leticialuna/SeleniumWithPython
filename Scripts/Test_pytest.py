import pytest


@pytest.fixture
def setup():
    print("Once before every method")
    yield
    print("Once after every method")

def testMethod1(setup):
    print("This is test method 1")

def testMethod2(setup):
    print("This is test method 2")

# executing using terminal 
# pytest -v -s Test_pytest.py
