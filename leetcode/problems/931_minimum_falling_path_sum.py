from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in range(1, m):
            for col in range(n):
                prev = [matrix[row-1][col]]
                if 0 <= col < n-1:
                    prev.append(matrix[row-1][col+1])
                if 1 <= col <= n-1:
                    prev.append(matrix[row-1][col-1])
                
                matrix[row][col] += min(prev)
        
        return min(matrix[-1])
