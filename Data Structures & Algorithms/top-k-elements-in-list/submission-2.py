from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        # buckets for 0 ~ n
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in cnt.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res