class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        
        while start <= end:
            mid = start + (end-start)//2
            
            if (1 + mid) * mid // 2 == n:
                return mid
            elif (1 + mid) * mid // 2 < n:
                start = mid + 1
            else:
                end = mid - 1
        if (1 + start) * start // 2 > n:
            return start - 1
        return start
