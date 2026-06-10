class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort + 2 pointers
        # -4, -1, -1, 0, 1, 2
        nums.sort()
        n = len(nums)
        res = []
        for i, num in enumerate(nums):
            if num > 0: # cannot 3sum to zero
                break
            if i > 0 and num == nums[i - 1]: # dup
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < -num:
                    l += 1
                elif nums[l] + nums[r] > -num:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res