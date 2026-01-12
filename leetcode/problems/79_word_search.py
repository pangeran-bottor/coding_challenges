from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        if any(word_count[c] > board_count.get(c, 0) for c in word_count):
            return False

        def dfs(k, r, c):
            if k == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if board[r][c] != word[k]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if dfs(k + 1, r + dr, c + dc):
                    return True

            board[r][c] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j):
                    return True

        return False
