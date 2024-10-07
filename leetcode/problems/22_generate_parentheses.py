from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate(curr: List[int], left: int, right: int):
            if len(curr) == 2 * n:
                ans.append("".join(curr))
                return

            if left < n:
                curr.append("(")
                _generate(curr, left=left + 1, right=right)
                curr.pop()

            if right < left:
                curr.append(")")
                _generate(curr, left=left, right=right + 1)
                curr.pop()

        ans: List[str] = []
        _generate([], left=0, right=0)
        return ans


if __name__ == "__main__":
    for g in Solution().generateParenthesis(n=3):
        print(g)
