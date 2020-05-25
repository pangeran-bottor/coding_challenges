from bisect import bisect_left
from collections import defaultdict


def solve(a, b):
	if a == b:
		return 0

	if b < a:
		if (a-b)%2==0:
			return 1
		else:
			return 2
	else:
		if (b-a)%2==0:
			return 2
		else:
			return 1

alist = []
alist.insert(3, 2)

t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	result = solve(a, b)
	print(result)