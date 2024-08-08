def min_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
    pass

def main():
    intervals = [(0, 30), (5, 10), (15, 20)]
    print(min_meeting_rooms(intervals))  # 2
    
    intervals = [(7, 10), (2, 4)]
    print(min_meeting_rooms(intervals))  # 1
    
    intervals = [(1, 5), (2, 6), (3, 8), (5, 7), (8, 9)]
    print(min_meeting_rooms(intervals))  # 3
    
if __name__ == "__main__":
    main()