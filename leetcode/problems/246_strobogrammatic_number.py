class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        digits_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        n = len(num)
        mid = n // 2
        for i in range(mid+1):
            left = num[i]
            right = num[n-i-1]

            if right not in digits_map:
                return False
            
            if digits_map[right] != left:
                return False
        
        return True
