# https://leetcode.com/contest/weekly-contest-198/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += numBottles//numExchange
            remain = numBottles % numExchange
            numBottles //= numExchange
            numBottles += remain
        return ans
