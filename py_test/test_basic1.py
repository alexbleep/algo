# content of test_sample.py
def funcPlusOne(x):
    return x + 1

def funcFalse(x):
    return False

def test_answer():
    assert funcPlusOne(3) == 5

def test_funcFalse():
    assert funcFalse(10) == True