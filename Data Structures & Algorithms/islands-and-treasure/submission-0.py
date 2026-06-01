from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        M, N = len(grid), len(grid[0])
        directions = [[1,0 ], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                nr, nc = dx + r, dy + c
                if nr in range(M) and nc in range(N) \
                and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))