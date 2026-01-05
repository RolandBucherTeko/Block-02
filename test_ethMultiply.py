import pytest
from ethMultiply import ethiopian_multiply
def test_ethiopian_multiply_kommutativ():
    assert ethiopian_multiply(7, 9) == ethiopian_multiply(9, 7) #Kommutativgesetz

@pytest.mark.parametrize("a, b, expected", [
    (1,5,5),
    (2,3,6),
    (5,0,0),
    (17,23,391),
    (12,12,144)
])
def test_ethiopian_multiply(a, b, expected):
    assert ethiopian_multiply(a, b) == expected
