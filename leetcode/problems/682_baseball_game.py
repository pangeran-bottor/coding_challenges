from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1 + num2)
            else:
                stack.append(int(op))

        return sum(stack)
