class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadans's Algo curSum vs MaxSum 
        curMin, glbMin, curMax, glbMax = 0, nums[0], 0, nums[0]
        total = 0
        for n in nums:
            total += n
            curMin = min(curMin + n, n)
            curMax = max(curMax + n, n)
            glbMin = min(glbMin, curMin)
            glbMax = max(glbMax, curMax)
        return max(glbMax, total - glbMin) if glbMax > 0 else glbMax