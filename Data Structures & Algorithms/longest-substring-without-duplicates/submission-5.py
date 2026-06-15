class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers
        seen, l, maxLen = {}, 0, 0
        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            maxLen = max(r - l + 1, maxLen)
            seen[s[r]] = r
        return maxLen