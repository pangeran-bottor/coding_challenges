class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = ord(t[0])
        for i in range(1, len(t)):
            result ^= ord(t[i])
        for i in range(len(s)):
            result ^= ord(s[i])
        return chr(result)
