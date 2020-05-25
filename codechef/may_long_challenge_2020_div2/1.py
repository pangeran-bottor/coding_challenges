def solve(N, X):
    minval = float("inf")
    maxval = float("-inf")

    cur_stack = []
    for x in X:
        if not cur_stack:
            cur_stack.append(x)
        else:
            if x - cur_stack[-1] <= 2:
                cur_stack.append(x)
            else:
                cur_len = len(cur_stack)
                minval = min(minval, cur_len)
                maxval = max(maxval, cur_len)
                cur_stack = [x]
        #print(cur_stack)
    if cur_stack:
        minval = min(minval, len(cur_stack))
        maxval = max(maxval, len(cur_stack))   
    return " ".join(map(str, [minval, maxval]))


T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    result = solve(N, X)
    print(result)