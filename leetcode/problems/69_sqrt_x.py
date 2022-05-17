class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        ans = 0
        while start <= end:
            mid = start + (end-start)//2
            if mid * mid <= x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans
