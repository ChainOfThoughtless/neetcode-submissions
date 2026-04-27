class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, curSum, L = float("inf"), 0, 0
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                res = min(res, R - L + 1)
                curSum -= nums[L]
                L += 1
        return res if res != float("inf") else 0