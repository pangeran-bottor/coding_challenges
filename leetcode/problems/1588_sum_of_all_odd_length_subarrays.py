from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        N = len(arr)
        for i in range(N):
            repeated = ((i+1)*(N-i) + 1)//2
            ans += arr[i] * repeated
        return ans
