class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen, left, seen = 0, 0, {}
        for i, c in enumerate(s):
            if c in seen:
                left = max(seen[c] + 1, left)
            seen[c] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen
                