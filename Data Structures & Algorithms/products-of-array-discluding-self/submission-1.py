class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCnt = 0
        for n in nums:
            if n == 0:
                zeroCnt += 1
                continue
            prod *= n
        
        res = [n for n in nums]
        for i in range(len(nums)):
            if (zeroCnt > 1):
                res[i] = 0
            elif zeroCnt == 1:
                res[i] = prod if nums[i] == 0 else 0
            else:
                res[i] = prod // nums[i]
        return res