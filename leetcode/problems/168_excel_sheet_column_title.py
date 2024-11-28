class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber:
            columnNumber -= 1
            ans.append(chr(columnNumber % 26 + 65))
            columnNumber //= 26
        return "".join(ans[::-1])
