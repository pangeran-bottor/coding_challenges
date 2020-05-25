n = int(input())

total = n*(n+1)//2
if total % 2:
    print("NO")
else:
    l1, l2 = [], []
    if n % 2:
        l1.append(n)
        for i in range(1, n//4 + 1):
            l1.append(i)
            l1.append(n-i)
        for j in range(n//4 + 1, n//2 + 1):
            l2.append(j)
            l2.append(n-j)
    else:
        for i in range(1, n//4 + 1):
            l1.append(i)
            l1.append(n-i+1)
        for j in range(n//4 + 1, n//2 + 1):
            l2.append(j)
            l2.append(n-j+1)

    print("YES")
    print(len(l1))
    print(" ".join(map(str, l1)))
    print(len(l2))
    print(" ".join(map(str, l2)))