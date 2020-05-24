# https://codeforces.com/contest/1360/problem/A

def solve(a, b):
    s = max(min(a, b)*2, max(a, b))
    return s*s


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = solve(a, b)
    print(result)
