a, b, c, k = map(int, input().split())

result = 0

m = [1, 0, -1]
options = [a, b, c]

idx = 0
while k > 0:
    get = min(k, options[idx])
    result += get*m[idx]

    idx += 1
    k -= get
print(result)