class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = 0
        subMax = nums[0]
        for n in nums:
            if currMax < 0:
                currMax = 0
            currMax += n
            subMax = max(currMax, subMax)
        return subMax