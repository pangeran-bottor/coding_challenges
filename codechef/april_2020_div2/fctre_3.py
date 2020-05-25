import itertools


def populate_prime_factors(): 
    MAX = 1000000
    factor = [0]*(MAX+1)

    factor[1] = 1

    for i in range(2,MAX):
        factor[i] = i
  
    for i in range(4,MAX,2): 
        factor[i] = 2
  
    i = 3
    while(i * i < MAX): 
        if (factor[i] == i): 
            j = i * i
            while(j < MAX):  
                if (factor[j] == j): 
                    factor[j] = i
                j += i
        i+=1
    return factor

def num_factor(n): 
    if (n == 1): 
        return 1
    ans = 1
    dup = factor[n]
    c = 1
    j = int(n / factor[n])
    while (j > 1): 
        if (factor[j] == dup): 
            c += 1
        else: 
            dup = factor[j]
            ans = ans * (c + 1)
            c = 1
        j = int(j / factor[j])
    ans = ans * (c + 1)
    return ans


class Engine:
    def __init__(self, N):
        self.N = N
        self.v = [[] for i in range(N+1)]
        self.nodevals = None
        self.vis = None
        self.stack = None

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



#factor = populate_prime_factors()
# memo = [0]*(10**6 + 1)
# memo[1] = 1
# for i in range(2, 10**6 + 1):
#     memo[i] = num_factor(i)
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
