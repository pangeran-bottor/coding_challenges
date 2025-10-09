from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = []
        step = 1
        d_idx = 0
        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                    rStart += directions[d_idx][0]
                    cStart += directions[d_idx][1]

                d_idx = (d_idx + 1) % 4
            step += 1
        return ans
