class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash set
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                #found the start
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        
        return longest