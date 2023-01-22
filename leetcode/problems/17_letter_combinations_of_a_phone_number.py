from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapper = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans = []

        n = len(digits)

        def backtrack(idx, seq):
            if len(seq) == n:
                if n > 0:
                    ans.append("".join(seq))
                return

            for ch in mapper[digits[idx]]:
                seq.append(ch)
                backtrack(idx + 1, seq)
                seq.pop()

        backtrack(0, [])
        return ans
