from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N // 2):
            s[i], s[N - i - 1] = s[N - i - 1], s[i]
