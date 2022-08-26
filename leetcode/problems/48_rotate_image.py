from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        mid = N // 2
        for layer in range(mid):
            for i in range(layer, N-1-layer):
                """
                layer will be the base part for top, right, bottom, left
                i will be the moving part
                
                top = matrix[layer][i]
                right = matrix[i][N-1-layer]
                bottom = matrix[N-1-layer][N-1-i]
                left = matrix[N-1-i][layer]
                """
                
                tmp = matrix[N-1-i][layer]
                matrix[N-1-i][layer] = matrix[N-1-layer][N-1-i]
                matrix[N-1-layer][N-1-i] = matrix[i][N-1-layer]
                matrix[i][N-1-layer] = matrix[layer][i]
                matrix[layer][i] = tmp
