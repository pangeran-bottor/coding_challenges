# https://leetcode.com/contest/weekly-contest-308/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)
