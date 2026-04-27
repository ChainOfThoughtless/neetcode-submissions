class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}
        for i, n in enumerate(nums):
            if len(idxMap) < 1:
                idxMap[n] = i
            else:
                if target - n in idxMap:
                    return [idxMap[target - n], i]
                idxMap[n] = i
