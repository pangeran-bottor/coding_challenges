def solve(N, a):
    counter = {}
    last_num = None
    while a:
        num = a.pop()
        if num == last_num:
            last_num = None
            continue
        else:
            last_num = num
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

    countlist = [(key, counter[key]) for key in counter]
    countlist.sort(key=lambda x: (-x[1], x[0]))
    return countlist[0][0]


T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    result = solve(N, a)
    print(result)