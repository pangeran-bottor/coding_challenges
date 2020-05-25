from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    sets = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    sets = [s for s in sets if len(s) > 0]
    return sets

def check_row(row, x):
    for el in row:
        if el < x:
            return False
    return True

n, m, x = map(int, input().split())
c_k_table = []
for _ in range(n):
    c_k_table.append(list(map(int, input().split())))

result = float("inf")
sets = powerset([i for i in range(n)])

for s in sets:
    k_rows = [0 for i in range(m)]

    cost = 0
    for idx in s:
        cur_c_k = c_k_table[idx]
        cost += cur_c_k[0]

        k_row = list(cur_c_k[1:])
        for i in range(m):
            k_rows[i] += k_row[i]
    
    if check_row(k_rows, x):
        result = min(result, cost)
if result == float("inf"):
    print(-1)
else:
    print(result)