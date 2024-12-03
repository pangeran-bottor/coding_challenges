from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        def fill(grid, r, c):
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in "WG":
                        break
                    grid[nr][nc] = "X"
                    nr, nc = nr + dr, nc + dc

        grid = [["U" for _ in range(n)] for _ in range(m)]
        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "G":
                    fill(grid, r, c)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "U":
                    ans += 1
        return ans
