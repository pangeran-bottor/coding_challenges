class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        N = len(columnTitle)
        for idx, char in enumerate(columnTitle):
            char_pos = (ord(char)-65) + 1
            result += (26 ** (N-idx-1)) * char_pos
            
        return result
