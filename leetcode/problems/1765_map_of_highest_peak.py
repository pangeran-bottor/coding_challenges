from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(n)] for _ in range(m)]
        cell_queue = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    height[i][j] = 0
                    cell_queue.append((i, j))

        height_layer = 1
        while cell_queue:
            curr_layer = len(cell_queue)

            for _ in range(curr_layer):
                r, c = cell_queue.popleft()
                for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1:
                        height[nr][nc] = height_layer
                        cell_queue.append((nr, nc))
            height_layer += 1

        return height
