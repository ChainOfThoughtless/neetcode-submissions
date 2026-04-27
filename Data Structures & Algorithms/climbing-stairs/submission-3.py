class Solution:
    def climbStairs(self, n: int) -> int:
        # 1: 1
        # 2: s1 + 1
        # 3: s1 + s2
        # 4: s3 + s2
        # n: s(n-1) + s(n-2)
        cache = {}
        
        def dp(stair):
            if stair <= 1:
                return 1
            if stair in cache:
                return cache[stair]
            cache[stair] = dp(stair - 1) + dp(stair - 2)
            return cache[stair]

        return dp(n)