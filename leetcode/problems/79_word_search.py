from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def is_possible(word, board):
            ch_counter = {}
            for ch in word:
                if ch not in ch_counter:
                    ch_counter[ch] = 0
                ch_counter[ch] += 1
            
            for row in board:
                for el in row:
                    if el in ch_counter:
                        ch_counter[el] -= 1
            
            for ch, count in ch_counter.items():
                if count > 0:
                    return False
            return True
        
        def dfs(board, word, i, j):
            if not word:
                return True
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            
            if board[i][j] != word[0]:
                return False
            
            tmp = board[i][j]
            board[i][j] = "#"
            for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                result = dfs(board, word[1:], i+r, j+c)
                if result:
                    return True
            board[i][j] = tmp
            return False
        
        if not is_possible(word, board):
            return False
        
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                result = dfs(board, word, i, j)
                if result:
                    return True
        return False
