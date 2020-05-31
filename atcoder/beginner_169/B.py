def solve(alist):
    if 0 in alist:
        return 0
    result = 1
    for a in alist:
        result *= a
        if result > 10**18:
            return -1
    return result

n = input()
alist = list(map(int, input().split()))
print(solve(alist))
