class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        idx, left, right = 0, 0, total
        while idx < len(nums):
            right -= nums[idx]
            if left == right:
                return idx
            left += nums[idx]
            idx += 1
        return -1