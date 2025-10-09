# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        d_idx = 0
        row, col = 0, 0

        while head:
            ans[row][col] = head.val
            nrow, ncol = row + directions[d_idx][0], col + directions[d_idx][1]

            if not (0 <= nrow < m and 0 <= ncol < n and ans[nrow][ncol] == -1):
                d_idx = (d_idx + 1) % 4
                nrow, ncol = row + directions[d_idx][0], col + directions[d_idx][1]

            row, col = nrow, ncol
            head = head.next
        return ans
