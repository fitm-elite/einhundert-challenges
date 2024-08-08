from insert_at_front import insert_at_front

def test_insert_at_front():
    assert insert_at_front(["apple", "banana", "cherry"]) == ["cherry", "banana", "apple"]
    