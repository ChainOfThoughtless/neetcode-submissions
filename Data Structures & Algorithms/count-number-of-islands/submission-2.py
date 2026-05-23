class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        # seen = {}
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            if 0 <= r < ROW and 0 <= c < COL:
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        dfs(nr, nc)
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res