class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        length = 0
        queue = deque()
        visited = set()
        visited.add((0, 0))
        queue.append((0, 0))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in directions:
                    if min(r + dr, c + dc) < 0 or \
                    r + dr == ROWS or c + dc == COLS or \
                    grid[r + dr][c + dc] == 1 or \
                    (r + dr, c + dc) in visited:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        return -1


        