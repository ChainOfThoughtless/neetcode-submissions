class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for n in nums:
            cnt[n] += 1
            
        idx = 0
        for val in range(len(cnt)):
            for _ in range(cnt[val]):
                nums[idx] = val
                idx += 1
        
        