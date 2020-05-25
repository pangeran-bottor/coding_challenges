def solve(n, x, a):
    a.sort(key=lambda x: -x)
    if a[0] < x:
        return 0

    cur_sum = a[0]
    cur_count = 1
    #print(a)
    for i in range(1, n):
        if (cur_sum + a[i]) / (cur_count + 1) >= x:
            cur_count += 1
            cur_sum += a[i]
            #print(cur_sum)
    return cur_count


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = solve(n, x, a)
    print(result)