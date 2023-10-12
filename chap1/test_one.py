from main import user


def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_name():
    name = 'Makiese'
    assert (user.get("name")) == name


def test_new():
    assert 'fizz' in 'fizzbuzz'
