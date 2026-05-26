"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        res = 0
        inout = defaultdict(int)
        for i in intervals:
            inout[i.start] += 1
            inout[i.end] -= 1
        
        for _, delta in sorted(inout.items()):
            rooms += delta
            res = max(res, rooms)
        
        return res