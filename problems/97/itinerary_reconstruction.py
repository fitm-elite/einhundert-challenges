def itinerary_reconstruction(tickets: list) -> list:
    pass

def main():
    tickets = [("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    print(itinerary_reconstruction(tickets))  # ["JFK", "MUC", "LHR", "SFO", "SJC"]
    
    tickets = [("JFK", "KUL"), ("JFK", "NRT"), ("NRT", "JFK")]
    print(itinerary_reconstruction(tickets))  # ["JFK", "NRT", "JFK", "KUL"]

if __name__ == "__main__":
    main()