class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadans's Algo curSum vs MaxSum 
        curMin, glbMin, curMax, glbMax = 0, nums[0], 0, nums[0]
        total = 0
        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            glbMax = max(glbMax, curMax)
            glbMin = min(glbMin, curMin)
        # total - glbMin will be > glbMax for all negative arr
        return max(glbMax, total - glbMin) if glbMax > 0 else glbMax