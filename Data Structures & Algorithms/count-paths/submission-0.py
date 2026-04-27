class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        def dp(r, c):
            if r == m or c == n: 
                return 0
            if r == m - 1 and c == n - 1: 
                return 1
            if cache[r][c] > 0:
                return cache[r][c]
            cache[r][c] = dp(r + 1, c) + dp(r, c + 1)
            return cache[r][c]
        return dp(0, 0)