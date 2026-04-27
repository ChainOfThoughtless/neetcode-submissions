class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dp(n):
            if n >= len(nums):
                return 0
            if n in cache:
                return cache[n]
            cache[n] = max((nums[n] + dp(n + 2)), dp(n + 1))
            return cache[n]
        return dp(0)