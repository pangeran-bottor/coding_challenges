from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filled = [el for el in row if el != "."]
            if len(filled) != len(set(filled)):
                return False

        for i in range(9):
            filled = [row[i] for row in board if row[i] != "."]
            if  len(filled) != len(set(filled)):
                return False

        for i in range(3):
            for j in range(3):
                filled = []
                for row in range(3*i, 3*(i+1)):
                    for col in range(3*j, 3*(j+1)):
                        val = board[row][col]
                        if val != ".":
                            filled.append(val)
                if len(filled) != len(set(filled)):
                    return False
        return True
