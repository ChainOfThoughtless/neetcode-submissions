class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = [] 
        def bt(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[idx])
            bt(idx + 1)
            subset.pop()
            bt(idx + 1)
        bt(0)
        return res
