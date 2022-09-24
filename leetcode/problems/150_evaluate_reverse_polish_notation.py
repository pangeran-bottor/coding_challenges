from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 1
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                # NOTE: using eval() would be significantly slower.
                if token == "+":
                    ans = (a + b)
                if token == "-":
                    ans = (a - b)
                if token == "*":
                    ans = (a * b)
                if token == "/":
                    ans = int(a / b)
                stack.append(ans)
            else:
                stack.append(int(token))
        if stack:
            return stack[0]
        return ans
