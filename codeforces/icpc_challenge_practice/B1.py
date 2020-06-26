import networkx as nx

n, m = map(int, input().split())
G = nx.Graph()
for _ in range(m):
    a, b = map(int, input().split())
    G.add_edge(a, b)

ans = nx.maximal_independent_set(G)
ans_list = [0 for i in range(n+1)]
for a in ans:
    ans_list[a] += 1
print(len(ans))
print(" ".join(map(str, ans_list[1:])))
