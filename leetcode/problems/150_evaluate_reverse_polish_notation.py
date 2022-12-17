from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "/": lambda x, y: int(x/y),
            "*": lambda x, y: x*y
        }

        stack = []
        for token in tokens:
            if token not in op_map:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(op_map[token](x, y))
        
        return stack.pop()
