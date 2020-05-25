def solve(N, a):
    mapper = {}
    for el in a:
        if el not in mapper:
            mapper[el] = 0
        mapper[el] += 1
    result = []
    
    visited = set()
    for el in a:
        if el not in visited:
            count = mapper[el]
            result.append(el + count)
            visited.add(el)
    return " ".join(map(str, result))


N = int(input())
a = list(map(int, input().split()))
result = solve(N, a)
print(result)