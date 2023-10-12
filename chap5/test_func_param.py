import cards
import pytest
from cards import Card


@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ("Write a book", "done"),
        ("second edition", "in prog"),
        ("create a course", "todo"),
    ],
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    
    cards_db.finish(index)
    
    card = cards_db.get_card(index)
    assert card.state == 'done'


def test_with_some_data(cards_db, non_empty_db):
    # initial_card = Card(summary=start_summary, state=start_state)
    cards_db.add_card(Card("first edition", state="in prog"))
    cards_db.add_card(Card("first edition", state="in prog"))
    assert cards_db.count() == 6
    

@pytest.mark.parametrize("start_state", ["done", "in prog", "todo"])
def test_finish_simple(cards_db, start_state):
    c = Card("Write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'
