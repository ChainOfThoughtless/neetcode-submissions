class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary seach within results 1 ~ max(piles)
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                r = k - 1
                res = min(k, res)
            else:
                l = k + 1
        
        return res