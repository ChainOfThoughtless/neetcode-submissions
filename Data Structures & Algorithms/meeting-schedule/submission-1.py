"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval:interval.start)
        if not intervals:
            return True
        schedule = [intervals[0]]
        for idx in range(1, len(intervals)):
            curr_meeting = intervals[idx]
            last_meeting = schedule[-1]
            if curr_meeting.start < last_meeting.end:
                return False
            schedule.append(curr_meeting)
        return True