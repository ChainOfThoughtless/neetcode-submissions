class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or \
           obstacleGrid[M - 1][N - 1] == 1:
           return 0
        
        memo = [[0] * N for _ in range(M)]
        
        def dp(r, c):
            if r == M or c == N or obstacleGrid[r][c] == 1:
                return 0
            if r == M - 1 and c == N - 1:
                return 1
            if memo[r][c] > 0:
                return memo[r][c]
            memo[r][c] = dp(r + 1, c) + dp(r, c + 1)
            return memo[r][c]
        
        return dp(0, 0)