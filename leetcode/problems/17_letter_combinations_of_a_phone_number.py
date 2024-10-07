from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def _generate(curr_idx: int, curr_s: str):
            if curr_s and len(curr_s) == n:
                ans.append(curr_s)
                return

            for idx in range(curr_idx, n):
                for ch in mapping[digits[idx]]:
                    curr_s += ch
                    _generate(curr_idx=idx + 1, curr_s=curr_s)
                    curr_s = curr_s[:-1]

        ans: List[str] = []
        n = len(digits)
        _generate(0, "")
        return ans


if __name__ == "__main__":
    digits = ""
    for c in Solution().letterCombinations(digits=digits):
        print(c)
