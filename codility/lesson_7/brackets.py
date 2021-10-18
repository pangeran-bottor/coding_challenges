# my result summary: https://app.codility.com/demo/results/trainingJEQAFK-TE9/

def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1

    stack = []
    for ch in S:
        if ch in "([{":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return 0

            if stack[-1] + ch in ("{}", "[]", "()"):
                stack.pop()
            else:
                return 0
    if len(stack) > 0:
        return 0
    return 1
