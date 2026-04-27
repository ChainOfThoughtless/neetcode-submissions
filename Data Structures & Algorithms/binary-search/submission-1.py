class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, start, end):
        if start > end:
            return -1
        mid = start + (end - start) // 2
        if nums[mid] < target:
            return self.binary_search(nums, target, mid + 1, end)
        if nums[mid]> target:
            return self.binary_search(nums, target, start, mid - 1)
        return mid