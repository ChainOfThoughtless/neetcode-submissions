class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        queue = deque()
        time = 0
        fresh = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and \
                    grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1