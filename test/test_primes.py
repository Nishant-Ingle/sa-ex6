import pytest

from flaskr import prime


def test_primes():
    expected = []
    result = prime.get_primes(0)
    assert expected == result
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    result = prime.get_primes(10)
    assert expected == result


def test_primes_wrong_input():
    assert [] == prime.get_primes(-1)
    with pytest.raises(TypeError):
        prime.get_primes("1")
