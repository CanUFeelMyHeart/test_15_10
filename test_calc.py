import pytest
from calc import add, sub, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 10

def test_sub():
    assert sub(5, 2) == 3

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)

    
