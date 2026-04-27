class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bt(nums, idx, subset, res):
            if idx >= len(nums):
                res.append(subset)
                return
            bt(nums, idx + 1, list(subset), res)
            subset.append(nums[idx])
            bt(nums, idx + 1, list(subset), res)
        
        subsets = []
        bt(nums, 0, [], subsets)
        return subsets
