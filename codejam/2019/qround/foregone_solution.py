def solve(N):
    l = []
    r = []

    for ch in N:
        if ch == "4":
            l.append("2")
            r.append("2")
        else:
            l.append(ch)
            #if r:
            r.append("0")
    l_str = "".join(l)
    r_str = "".join(r)
    return " ".join([l_str, r_str])


T = int(input())
for t in range(T):
    N = input()
    result = solve(N)
    print("Case #{}: {}".format(t+1, result))