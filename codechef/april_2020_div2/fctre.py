import math as mt 

  
MAXN = 1000001

spf = [0 for i in range(MAXN)] 
def sieve(): 
    spf[1] = 1
    for i in range(2, MAXN): 
        spf[i] = i 
    for i in range(4, MAXN, 2): 
        spf[i] = 2
  
    for i in range(3, mt.ceil(mt.sqrt(MAXN))): 
        if (spf[i] == i): 
            for j in range(i * i, MAXN, i):  
                if (spf[j] == j): 
                    spf[j] = i 
  
def prime_factors(n): 
    factors = []
    while (n != 1): 
        factors.append(spf[n]) 
        n = n // spf[n] 
    return factors


class Engine:
    def __init__(self, N):
        self.N = N
        self.v = [[] for i in range(N+1)]
        self.nodevals = None
        self.vis = None
        self.stack = None
        self.dfs_memo = {}

    def set_nodevals(self, nodevals):
        self.nodevals = [0] + nodevals

    def add_edge(self, v1, v2):
        self.v[v1].append(v2)
        self.v[v2].append(v1)

    def dfs(self, vis, v1, v2, stack):
        stack.append(v1)
        if v1 == v2:
            return
        vis[v1] = True

        flag = 0
        if len(self.v[v1]) > 0:
            for j in self.v[v1]:
                if not vis[j]:
                    self.dfs(vis, j, v2, stack)
                    flag = 1

        if flag == 0:
            del stack[-1] 

    def solve_for_path(self, v1, v2):

        self.vis = [0 for i in range(self.N+1)]
        self.stack = []
        self.dfs(self.vis, v1, v2, self.stack)

        factormap = {}
        for el in self.stack:
            nodeval = self.nodevals[el]
            for p in prime_factors(nodeval):
                if p not in factormap:
                    factormap[p] = 0
                factormap[p] += 1
        #print(factormap)
        result = 1
        mod = 10**9 + 7
        for f in factormap:
            result *= (factormap[f] + 1)
            result %= mod
        return result

sieve()
memo = [[], []]
for i in range(2, MAXN + 1):
    memo[i] = prime_factors(i)
#print("sieve done")
T = int(input())
for _ in range(T):
    N = int(input())
    engine = Engine(N)
    for _ in range(N-1):
        v1, v2 = map(int, input().split())
        engine.add_edge(v1, v2)
    vals = list(map(int, input().split()))
    engine.set_nodevals(vals)
    
    Q = int(input())
    for _ in range(Q):
        v1, v2 = map(int, input().split())
        result = engine.solve_for_path(v1, v2)
        print(result)
