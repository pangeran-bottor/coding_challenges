# https://codeforces.com/contest/1360/problem/B

def solve(alist):
    alist.sort()
    result = float("inf")
    for i in range(1, len(alist)):
        result = min(result, abs(alist[i]-alist[i-1]))
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    alist = list(map(int, input().split()))
    result = solve(alist)
    print(result)
