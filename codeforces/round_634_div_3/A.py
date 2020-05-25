def solve(n):
    if n < 2:
        return 0

    if n % 2 == 0:
        result = n//2 - 1
        return result
    return n//2
    
t = int(input())
for _ in range(t):
    n = int(input())
    result = solve(n)
    print(result)