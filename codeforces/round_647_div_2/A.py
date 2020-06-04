# https://codeforces.com/contest/1362/problem/A


def solve(a, b):
    def helper(a, b):
        if a == b:
            return 0
        if a < b:
            return helper(b, a)
        result = 0
        while a > b:
            if a % 2:
                return -1
            else:
                a //= 2
                result += 1
            if a == b:
                return result
        return -1

    ans = helper(a, b)
    if ans == -1:
        return ans

    result = ans // 3
    ans %= 3
    result += ans // 2
    ans %= 2
    if ans:
        result += ans
    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result)