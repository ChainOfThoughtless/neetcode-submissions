class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            if not self.canFinish(piles, h, k):
                l = k + 1
            else:
                r = k
        return r

    def canFinish(self, piles, h, rate):
        totalHr = 0
        for banana in piles:
            totalHr += math.ceil(banana / rate)
        return totalHr <= h