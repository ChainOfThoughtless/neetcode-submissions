class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        ans = 0
        for _ in range(32):
            if n & mask:
                ans += 1
            mask <<= 1
        return ans