class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for num in nums:
            if l < 1 or num != nums[l - 1]:
                nums[l] = num
                l += 1
        return l