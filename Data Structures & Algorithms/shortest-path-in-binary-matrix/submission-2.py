class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1
        visited = set()
        queue = deque()
        visited.add((0, 0))
        queue.append((0, 0))

        directions = [[1, 0], [-1, 0], [1, 1], [-1, -1], 
                      [0, 1], [0, -1], [1, -1], [-1, 1]]
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == N - 1 and c == N - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N and \
                       grid[nr][nc] == 0 and \
                       (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
        return -1