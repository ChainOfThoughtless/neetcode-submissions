class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            l, r, t = i + 1, n - 1, -nums[i]
            while l < r:
                if nums[l] + nums[r] > t:
                    r -= 1
                elif nums[l] + nums[r] < t:
                    l += 1
                elif nums[l] + nums[r] == t:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res