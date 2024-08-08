from itinerary_reconstruction import itinerary_reconstruction

def test_itinerary_reconstruction():
    tickets = [("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    result = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert itinerary_reconstruction(tickets) == result
    
    tickets = [("JFK", "KUL"), ("JFK", "NRT"), ("NRT", "JFK")]
    result = ["JFK", "NRT", "JFK", "KUL"]
    assert itinerary_reconstruction(tickets) == result