n, m, a = map(int, input().split())

r = n//a + (1 if n%a>0 else 0)
c = m//a + (1 if m%a>0 else 0)
print(r*c)