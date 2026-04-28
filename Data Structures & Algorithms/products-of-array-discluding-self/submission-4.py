class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #build surfix
        n = len(nums)
        surfix = [1] * n
        for i in range(n - 1, -1, -1):
            surfix[i] = nums[i] * surfix[i + 1] if i + 1 <= n - 1 else nums[i]
        
        #build prefix while l -> r
        res = [0] * n
        prefix = [1] * n
        for i in range(n):
            prefix[i] = nums[i] * prefix[i - 1] if i - 1 >= 0 else nums[i]
            left = prefix[i - 1] if i - 1 >= 0 else 1
            right = surfix[i + 1] if i + 1 <= n - 1 else 1
            res[i] = left * right
        return res