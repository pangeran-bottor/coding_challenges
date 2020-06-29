
def sub_lists(list1): 
    sublist = [] 
    for i in range(len(list1) + 1): 
        for j in range(i + 1, len(list1) + 1): 
            sub = list1[i:j] 
            sublist.append(" ".join(map(str, sub))) 
    sublist = list(set(sublist))
    return sublist 


def solve(items):
    mapper = {}
    for item in items:
        subitems = sub_lists(item.split())
        #print(subitems)
        for word in subitems:
            if word not in mapper:
                mapper[word] = 0
            mapper[word] += 1
    return mapper



t = int(input())
for i in range(t):
    N, Q = map(int, input().split())
    items = []
    for _ in range(N):
        items.append(input())
    mapper = solve(items)
    print("Case {}:".format(i+1))
    for _ in range(Q):
        q = input()
        print(mapper.get(q, 0))
