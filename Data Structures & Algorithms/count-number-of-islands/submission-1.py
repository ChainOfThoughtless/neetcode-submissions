class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nr >= M or nc < 0 or nc >= N or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
        
        for r in range(M):
            for c in range(N):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1

        return res