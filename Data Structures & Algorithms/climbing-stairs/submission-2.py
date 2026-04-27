class Solution:
    def climbStairs(self, n: int) -> int:
        # 1: 1
        # 2: s1 + 1
        # 3: s1 + s2
        # 4: s3 + s2
        # n: s(n-1) + s(n-2)
        if n <= 1:
            return 1
        cache = [1, 2]
        idx = 2
        while idx < n:
            tmp = cache[1]
            cache[1] = cache[0] + cache[1]
            cache[0] = tmp
            idx += 1
        return cache[1]