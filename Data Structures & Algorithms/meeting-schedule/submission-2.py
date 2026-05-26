"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        timesheet = defaultdict(int)
        for i in intervals:
            timesheet[i.start] += 1
            timesheet[i.end] -= 1
        
        rooms = 0
        max_rooms = 0
        for _, delta in sorted(timesheet.items()):
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        return False if max_rooms > 1 else True

