# https://cses.fi/problemset/task/1068/

def solve(n):
    steps = [n]
    while n != 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        steps.append(n)
    return " ".join(map(str, steps))


n = int(input())
result = solve(n)
print(result)