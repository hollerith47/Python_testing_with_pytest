import pytest

from main import user


@pytest.mark.xfail()
def test_failing():
    assert (1, 2, 3) == (3, 2, 1)


@pytest.mark.xfail()
def test_name():
    name = 'Herman'
    assert (user.get("name")) == name


@pytest.mark.xfail()
def test_new():
    assert 'fizz' not in 'fizzbuzz'
