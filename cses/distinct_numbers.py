n = int(input())
x = list(map(int, input().split()))

xset = set()
for el in x:
    xset.add(el)
print(len(xset))