class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ct = high - low + 1
        if ct % 2 == 0:
            return ct // 2
        return (low % 2) + (ct-1) // 2
