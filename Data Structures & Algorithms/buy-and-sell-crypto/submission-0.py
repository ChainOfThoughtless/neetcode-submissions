class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, res = prices[0], 0
        for price in prices:
            low = min(price, low)
            res = max(price - low, res)
        return res