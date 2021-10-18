# my result summary: https://app.codility.com/demo/results/trainingKVJ879-VJ3/

def solution(H):
    # write your code in Python 3.6
    ans = 0
    stack = []
    for num in H:
        if len(stack) == 0:
            stack.append(num)
            ans += 1
        else:
            if num > stack[-1]:
                stack.append(num)
                ans += 1
            else:
                while len(stack) > 0:
                    if stack[-1] > num:
                        stack.pop()
                    elif stack[-1] == num:
                        break
                    else:
                        stack.append(num)
                        ans += 1
                if len(stack) == 0:
                    stack.append(num)
                    ans += 1
    return ans
