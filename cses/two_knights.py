def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 6

    all_pos = (n**2)*(n**2-1)//2
    neg = 2*(n-2+1)*(n-3+1)*2
    return all_pos-neg


n = int(input())
for i in range(1, n+1):
    print(solve(i))
    