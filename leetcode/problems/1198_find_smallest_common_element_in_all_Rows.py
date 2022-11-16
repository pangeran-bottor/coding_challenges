from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        mem = [0 for _ in range(10**4 + 1)]
        
        m = len(mat)
        for row in mat:
            for el in row:
                mem[el] += 1
                if mem[el] == m:
                    return el
        
        return -1
