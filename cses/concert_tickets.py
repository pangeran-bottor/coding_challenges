from bisect import bisect_left


n, m = map(int, input().split())
hlist = list(map(int, input().split()))
tlist = list(map(int, input().split()))

mapper = {}
for h in hlist:
    if h not in mapper:
        mapper[h] = 0
    mapper[h] += 1

for t in tlist:
    cur_keys = [k for k in mapper if mapper[k] > 0]
    cur_keys.sort()

    idx = bisect_left(cur_keys, t)
    if idx == len(cur_keys):
        print(cur_keys[-1])
        mapper[cur_keys[-1]] -= 1
    elif cur_keys[idx] == t:
        print(cur_keys[idx])
        mapper[cur_keys[idx]] -= 1
    elif idx-1>0 and cur_keys[idx-1] < t:
        print(cur_keys[idx-1])
        mapper[cur_keys[idx-1]] -= 1
    else:
        print(-1)