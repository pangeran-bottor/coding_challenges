# https://codeforces.com/contest/1360/problem/C

def solve(alist):
    alist.sort()
    odd = 0
    even = 0
    consecutives = []
    for i in range(len(alist)):
        if alist[i] % 2:
            odd += 1
        else:
            even += 1
        if i > 0:
            if alist[i]-alist[i-1] == 1:
                consecutives.append([alist[i-1], alist[i]])
    #print(odd, even, consecutives)

    if odd % 2 == 0 and even % 2 == 0:
        return "YES"
    if odd % 2 == 1 and even % 2 == 1:
        if len(consecutives) > 0:
            return "YES"
        else:
            return "NO"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    alist = list(map(int, input().split()))
    result = solve(alist)
    print(result)