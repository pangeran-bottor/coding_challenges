from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(curr_word: str, row: int, col: int):
            if len(curr_word) == 0:
                return True

            if row < 0 or row >= R or col < 0 or col >= C:
                return False

            if curr_word[0] != board[row][col]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nrow, ncol = row + dr, col + dc
                if backtrack(curr_word=curr_word[1:], row=nrow, col=ncol):
                    return True

            board[row][col] = temp
            return False

        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                ret = backtrack(word, i, j)
                if ret:
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "SEE"
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCB"
    print(Solution().exist(board=board, word=word))
