class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, L, maxF, maxLen = {}, 0, 0, 0
        # maxF = max(count.values()) get the max frequency value at O(26) complexity
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            #windowSize = R - L + 1
            #maxF = max(count.values())
            #diff = windowSize - maxF
            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            maxLen = max(maxLen, R - L + 1)
        return maxLen