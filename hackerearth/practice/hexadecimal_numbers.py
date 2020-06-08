# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/yet-another-easy-problem-1f3273a0/


import math
 
def f(n):
    nhex_str = hex(n).replace("0x", "")
    nhex = 0
    for el in nhex_str:
        if el in "1234567890":
            nhex += int(el)
        else:
            nhex += (10 + "abcdef".index(el))
    return nhex
 
 
def generate_dp():
    dp = [0]
    for i in range(1, 10**5 + 1):
        if math.gcd(i, f(i)) > 1:
            dp.append(dp[-1] + 1)
        else:
            dp.append(dp[-1])
    return dp
 
def solve(L, R, dp):
    return dp[R] - dp[L-1]
 
 
dp = generate_dp()
T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    ans = solve(L, R, dp)
    print(ans)
