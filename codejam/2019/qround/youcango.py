def solve(N, P):
    result = ""
    for ch in P:
        if ch == "E":
            result += "S"
        else:
            result += "E"
    return result

T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    result = solve(N, P)
    print("Case #{}: {}".format(t+1, result))