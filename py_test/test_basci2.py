# content of test_sample.py
def funcPlusTwo(x):
    return x + 2

def test_funcPlusTwo():
    assert funcPlusTwo(3) == 5

def test_funcPlusTwo2():
    assert funcPlusTwo(9) == 11