def solve(S):
    S = list(S)
    ans = 0
    cur_pair = []
    while S:
        if len(cur_pair) < 2:
            cur_pair.append(S.pop())
        elif "x" in cur_pair and "y" in cur_pair:
            ans += 1
            cur_pair = []
        else:
            cur_pair.pop(0)
        if len(S) == 0 and "x" in cur_pair and "y" in cur_pair:
            ans += 1
    return ans


T = int(input())
for _ in range(T):
    S = input()
    result = solve(S)
    print(result)
