from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        
        left = 0
        right = n-1
        up = 0
        down = n-1
        
        count = 1
        while count <= n*n:
            for idx in range(left, right+1):
                result[up][idx] = count
                count += 1
            up += 1
            
            for idx in range(up, down+1):
                result[idx][right] = count
                count += 1
            right -= 1
            
            for idx in range(right, left-1, -1):
                result[down][idx] = count
                count += 1
            down -= 1
            
            for idx in range(down, up-1, -1):
                result[idx][left] = count
                count += 1
            left += 1
        
        return result
