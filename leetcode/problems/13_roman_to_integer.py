class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        N = len(s)
        ans = mapping[s[0]]

        for i in range(1, N):
            if mapping[s[i]] > mapping[s[i - 1]]:
                ans -= mapping[s[i - 1]]
                ans += mapping[s[i]] - mapping[s[i - 1]]
            else:
                ans += mapping[s[i]]
        return ans
