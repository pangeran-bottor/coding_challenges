def solve(a, b, c):
	counter = 0

	counter1 = float("inf")
	for el in range(a, b+1):
		if b%el == 0:
			if el-a < counter:
				



t = int(input())
for _ in range(t):
	a, b, c = map(int, input().split())
	count, triple = solve(a, b, c)
	print(count)
	print(triple)