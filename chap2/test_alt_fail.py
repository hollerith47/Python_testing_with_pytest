import pytest
from cards import Card


def test_with_fail():
    c1 = Card("sit there", "brian")
    c2 = Card("do something", "Herman")
    if c1 != c2:
        pytest.fail("They don't match")
