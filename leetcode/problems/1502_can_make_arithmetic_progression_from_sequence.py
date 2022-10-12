from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val, max_val = min(arr), max(arr)
        n = len(arr)
        
        # the differences can not be distributed evenly
        if (max_val - min_val) % (n-1) != 0 :
            return False
        
        # contains elements with the same value
        if max_val == min_val:
            return True
        
        # contains duplicates while diff != 0
        if n != len(set(arr)):
            return False
        
        diff = (max_val - min_val) // (n-1)
        for i in range(1, n):
            if abs(arr[i] - arr[i-1]) % diff != 0:
                return False
        return True
