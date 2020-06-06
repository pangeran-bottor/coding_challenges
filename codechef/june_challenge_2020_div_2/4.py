def solve(ts):
    if ts % 2:
        return (ts-1)//2
    
    count_to_odd = 0
    t = ts
    while t % 2 == 0:
        t //= 2
        count_to_odd += 1
    #print(count_to_odd)

    start = 2**count_to_odd
    ans = 0
    if (ts // start) % 2 == 0:
        ans += ((ts // start))//2
    else:
        ans += ((ts // start)-1)//2
    return ans


T = int(input())
for _ in range(T):
    ts = int(input())
    result = solve(ts)
    print(result)