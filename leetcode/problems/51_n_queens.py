from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generate(idx, cur):
            if len(cur) == n:
                board = [["." for _ in range(n)] for _ in range(n)]
                for idx, c in enumerate(cur):
                    board[idx][c] = "Q"
                board = ["".join(row) for row in board]
                ans.append(board)
                return

            for i in range(n):
                if i in cur:
                    continue
                if len(cur) > 0:
                    ncur = len(cur)
                    invalid = False
                    for cidx, val in enumerate(cur):
                        if abs(i - val) == (ncur - cidx):
                            invalid = True
                    if invalid:
                        continue
                cur.append(i)
                generate(i + 1, cur)
                cur.pop()

        ans = []
        generate(0, [])
        return ans
