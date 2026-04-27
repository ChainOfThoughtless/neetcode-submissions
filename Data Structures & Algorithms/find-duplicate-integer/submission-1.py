class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        phase = 1
        while True:
            slow = nums[slow]
            if phase == 1:
                fast = nums[nums[fast]]
            else:
                fast = nums[fast]
            if slow == fast:
                if phase != 1:
                    return fast
                fast = 0
                phase += 1
        