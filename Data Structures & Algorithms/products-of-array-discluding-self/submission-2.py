class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix, suffix = list(nums), nums[:]
        for i in range(1, l):
            prefix[i] *= prefix[i - 1]
            suffix[l - i - 1] *= suffix[l - i]
        res = [0] * l
        for i in range(l):
            left = prefix[i - 1] if (i - 1) >= 0 else 1
            right = suffix[i + 1] if (i + 1) <= (l - 1) else 1
            res[i] = left * right
        return res