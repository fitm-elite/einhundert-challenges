from meeting_room_ii import min_meeting_rooms

def test_meeting_room_ii():
    assert min_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
    assert min_meeting_rooms([(7, 10), (2, 4)]) == 1
    assert min_meeting_rooms([(1, 5), (2, 6), (3, 8), (5, 7), (8, 9)]) == 3