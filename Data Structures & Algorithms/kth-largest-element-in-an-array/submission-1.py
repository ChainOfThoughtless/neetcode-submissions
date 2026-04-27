class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k #index of kth largest in ascending sorted order
        def qs(l, r): # -> pos
            pivot, pos = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1
            nums[pos], nums[r] = nums[r], nums[pos]
            if pos > k: return qs(l, pos - 1)
            if pos < k: return qs(pos + 1, r)
            return nums[pos]
        return qs(0, len(nums) - 1)