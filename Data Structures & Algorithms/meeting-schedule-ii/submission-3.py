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
        
        for i in sorted(inout.keys()):
            rooms += inout[i]
            res = max(res, rooms)
        
        return res