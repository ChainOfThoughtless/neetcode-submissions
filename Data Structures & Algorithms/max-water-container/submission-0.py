class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans, l, r = 0, 0, len(heights) - 1
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            ans = max(ans, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans