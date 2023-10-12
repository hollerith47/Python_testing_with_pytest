from cards import Card


def test_finish(cards_db):
    for c in [
        Card('Write a book', state="done"),
        Card('second edition', state="in prog"),
        Card("create course", state="todo")
    ]:
        index = cards_db.add_card(c)
        cards_db.finish(index)
        card = cards_db.get_card(index)
        assert card.state == "done"
