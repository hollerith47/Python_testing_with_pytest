import pytest
from cards import Card


# @pytest.mark.xfail
def test_equality_fail():
    c1 = Card("sit there", "Herman")
    c2 = Card("do something", "okken")
    assert c1 == c2


if __name__ == "__main__":
    test_equality_fail()
