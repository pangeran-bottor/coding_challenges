def solve(n):
    if n == 1:
        return 1
    if n < 4:
        return "NO SOLUTION"

    result = []
    mid = n//2
    left = 1
    right = n//2 + 1

    while right<=n:
        result.append(right)
        if left <= mid:
            result.append(left)
        left += 1
        right += 1

    return " ".join(map(str, result))


n = int(input())
result = solve(n)
print(result)