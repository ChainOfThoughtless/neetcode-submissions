class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        seen = {(0, 0)}
        directions = [(1, 2), (1, -2), (2, 1), (2, -1),
                      (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        q = deque([(0, 0, 0)])
        while q:
            px, py, steps = q.popleft()
            if px == x and py == y: #found
                return steps
            for dx, dy in directions:
                nx, ny = abs(px + dx), abs(py + dy)
                if 0 <= nx <= x + 2 and \
                    0 <= ny <= y + 2 and \
                    (nx, ny) not in seen:
                    q.append((nx, ny, steps + 1))
                    seen.add((nx, ny))
        return
