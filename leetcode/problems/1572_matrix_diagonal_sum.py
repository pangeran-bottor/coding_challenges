from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        result = 0
        for x, row in enumerate(mat):
            result += mat[x][x]
            result += mat[x][N-x-1]
        if N % 2 == 1:
            result -= mat[N//2][N//2]
        return result
