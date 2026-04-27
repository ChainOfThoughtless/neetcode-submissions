class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        def bt(idx, subsetSum):
            if idx >= len(nums):
                return
            if subsetSum == target:
                res.append(subset.copy())
                return
            if subsetSum > target:
                return
            subset.append(nums[idx])
            bt(idx, subsetSum + nums[idx])
            subset.pop()
            bt(idx + 1, subsetSum)
        
        bt(0, 0)
        return res