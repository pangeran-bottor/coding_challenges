from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        ans = []
        
        left, right = 0, C-1
        top, bottom = 0, R-1
        
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            
            if top > bottom:
                break
            
            for j in range(top, bottom+1):
                ans.append(matrix[j][right])
            right -= 1
            
            if left > right:
                break
            
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans
