from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        row_counts = [0 for _ in range(row)]
        col_counts = [0 for _ in range(col)]

        mat_map = {}
        for i in range(row):
            for j in range(col):
                mat_map[mat[i][j]] = [i, j]

        for i in range(len(arr)):
            curr_row, curr_col = mat_map[arr[i]]
            row_counts[curr_row] += 1
            col_counts[curr_col] += 1
            if row_counts[curr_row] == col:
                return i
            if col_counts[curr_col] == row:
                return i
