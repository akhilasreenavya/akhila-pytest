import pytest
from src.my_methods import add_numbers,multiply_numbers


def test_add_numbers():
    assert add_numbers(2,3) == 5
    print("passed")
    assert add_numbers(10,5) == 15
    assert add_numbers(-1,1)==0

def test_multiply_numbers():
    assert multiply_numbers(4,5) == 20
