from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()

        result = 0
        for a in arr1:
            start, end = 0, len(arr2) - 1
            
            found = False
            while start <= end:
                mid = start + (end-start)//2
                
                if abs(a - arr2[mid]) <= d:
                    found = True
                    break
                
                # adjust mid position so we get closer to a
                if a < arr2[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
                
            if not found:
                result += 1
        return result
