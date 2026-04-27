class Solution:
    def climbStairs(self, n: int) -> int:
        # 1: 1
        # 2: s1 + 1
        # 3: s1 + s2
        # 4: s3 + s2
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)