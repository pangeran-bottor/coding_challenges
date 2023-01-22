from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(seq, left=0, right=0):
            if len(seq) == 2 * n:
                ans.append("".join(seq))
                return

            if left < n:
                seq.append("(")
                backtrack(seq, left + 1, right)
                seq.pop()

            if right < left:
                seq.append(")")
                backtrack(seq, left, right + 1)
                seq.pop()

        backtrack([])
        return ans
