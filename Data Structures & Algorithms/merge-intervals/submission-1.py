class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for slot in intervals[1:]:
            if res[-1][1] >= slot[0]:
                res[-1][1] = max(res[-1][1], slot[1])
            else:
                res.append(slot)
        return res
