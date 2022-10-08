import collections
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        col = collections.defaultdict(list)
        for x, y in points:
            col[x].append(y)
        
        ans = float("inf")
        lastx = {}
        
        sorted_col_key = sorted(col)
        for x in sorted_col_key:
            column = col[x]
            column.sort()
            
            for i, y2 in enumerate(column):
                for j in range(i):
                    y1 = column[j]
                    
                    if (y1, y2) in lastx:
                        ans = min(ans, ((x-lastx[(y1, y2)]) * (y2-y1)))
                    lastx[(y1, y2)] = x
        if ans == float("inf"):
            return 0
        return ans
