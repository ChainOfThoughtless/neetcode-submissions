class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        next, skip = nums[-2], nums[-1]
        idx = len(nums) - 3
        while idx >= 0:
            tmp = next
            next = max(nums[idx] + skip, next)
            skip = tmp
            idx -= 1
            print(next, skip)
        return next  