from itertools import combinations
from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        
        ans = 0

        """
            TODO: try to generate combinations without built-in function
        """
        for selected_cols in combinations(range(N), numSelect):
            num_covered = 0
            for i in range(M):
                covered = True
                for j in range(N):
                    if matrix[i][j] == 1 and j not in selected_cols:
                        covered = False
                        break
                if covered:
                    num_covered += 1
            ans = max(ans, num_covered)
        return ans
