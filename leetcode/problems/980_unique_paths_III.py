from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        non_obstacles = 0
        start_row, start_col = 0, 0
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == 1:
                    start_row, start_col = r, c
                if cell >= 0:
                    non_obstacles += 1

        path_count = 0

        def backtrack(row, col, remain):
            nonlocal path_count

            if grid[row][col] == 2 and remain == 1:
                path_count += 1
                return

            cell = grid[row][col]
            grid[row][col] = -3
            remain -= 1

            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue

                if grid[next_row][next_col] < 0:
                    continue

                backtrack(next_row, next_col, remain)

            grid[row][col] = cell

        backtrack(start_row, start_col, non_obstacles)
        return path_count
