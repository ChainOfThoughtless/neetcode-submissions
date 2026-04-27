class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        while slow < len(nums):
            fast = nums[slow] - 1
            if slow == nums[slow] - 1:
                slow += 1
                continue
            if fast == nums[fast] - 1:
                return nums[fast]
            nums[slow], nums[fast] = nums[fast], nums[slow]
        return 