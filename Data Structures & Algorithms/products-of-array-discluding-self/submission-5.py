class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        #build surfix
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        #build prefix while l -> r
        surfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= surfix
            surfix *= nums[i]
        
        return res