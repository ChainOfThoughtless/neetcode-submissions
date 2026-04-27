class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        for n in nums:
            if n in exist:
                return True
            exist.add(n)
        return False