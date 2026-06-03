class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        missing_ranges = []
        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges
        
        # lower ~ nums[0]
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])
        
        # between nums
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1: # consecutive
                continue
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])

        # nums[-1] ~ upper
        if nums[-1] < upper:
            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges