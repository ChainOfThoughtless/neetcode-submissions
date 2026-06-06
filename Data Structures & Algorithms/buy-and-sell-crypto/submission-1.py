class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_low = float('inf')
        max_p = 0
        for i in range(len(prices)):
            max_p = max(max_p, prices[i] - curr_low)
            curr_low = min(curr_low, prices[i])
        return max_p