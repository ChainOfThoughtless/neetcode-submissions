class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.dfs(grid, row, col) # recursively mark visited
        return count
    
    def dfs(self, grid, r, c):
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r >= ROWS or \
            c >= COLS or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
        