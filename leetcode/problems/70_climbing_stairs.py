class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        f0 = 1
        f1 = 2
        for _ in range(3, n + 1):
            f0, f1 = f1, f0 + f1

        return f1
