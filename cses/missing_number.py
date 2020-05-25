def solve(n, arr):
    total = n*(n+1)//2
    return total-sum(arr)


n = int(input())
arr = list(map(int, input().split()))
result = solve(n, arr)
print(result)