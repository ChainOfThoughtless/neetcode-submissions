class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(ROW, COL):
            q = deque()
            q.append((ROW, COL))
            while q:
                r, c = q.popleft()
                grid[r][c] = '0'
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    pair = (nr, nc)
                    if 0 <= nr < ROWS and 0 <= nc < COLS and \
                        pair not in seen and \
                        grid[nr][nc] == '1':
                        q.append(pair)
                        seen.add(pair)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    seen.add((r, c))
                    bfs(r, c)
                    res += 1
        
        return res