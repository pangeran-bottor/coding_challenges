from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        values = []
        for row in range(9):
            for col in range(9):
                ch = board[row][col]
                if ch == ".":
                    continue

                values.append((row, ch))
                values.append((ch, col))
                values.append((row // 3, col // 3, ch))
        return len(values) == len(set(values))
