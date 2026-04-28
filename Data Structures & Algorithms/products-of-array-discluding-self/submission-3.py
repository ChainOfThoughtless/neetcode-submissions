class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros, prod = 0, 1
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n
        res = [0] * len(nums)
        if zeros > 1:
            return res
        for i, n in enumerate(nums):
            if zeros == 1:
                res[i] = prod if n == 0 else 0
            else: # zeros == 0
                res[i] = prod // n
        return res