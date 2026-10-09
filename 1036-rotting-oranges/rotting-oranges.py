from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (0 <= row < rows and 0 <= col < cols
                            and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))

            time += 1

        return time if fresh == 0 else -1