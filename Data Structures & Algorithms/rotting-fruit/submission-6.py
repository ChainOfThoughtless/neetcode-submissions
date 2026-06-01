class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        fresh = 0
        time = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        # iterate grid to enqueue rotten and track fresh count
        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        # layered BFS for time and infect fresh fruit
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dx, dy in directions:
                    nr, nc = dx + r, dy + c
                    if 0 <= nr < M and 0 <= nc < N \
                       and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1