from cards import Card


class TestEquality:
    def test_equality(self):
        c1 = Card("something", 'brian', 'todo', 123)
        c2 = Card("something", 'brian', 'todo', 123)
        assert c1 == c2
    
    def test_equality_with_diff_ids(self):
        c1 = Card("something", 'brian', 'todo', 123)
        c2 = Card("something", 'brian', 'todo', 4567)
        assert c1 == c2
    
    def test_inequality(self):
        c1 = Card("something", 'brian', 'todo', 123)
        c2 = Card("completely different", 'okken', 'done', 4567)
        assert c1 != c2
    
    def test_from_dict(self):
        c1 = Card("something", 'brian', 'todo', 123)
        c2_dict = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": "123",
        }
        c2 = Card.from_dict(c2_dict)
        assert c1 == c2
    
    def test_to_dict(self):
        c1 = Card("something", "brian", "todo", 123)
        c2 = c1.to_dict()
        c2_expected = {
            "summary": "something",
            "owner": "brian",
            "state": "todo",
            "id": 123,
        }
        assert c2 == c2_expected