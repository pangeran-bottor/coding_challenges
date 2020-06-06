def solve(N):
    l = [i for i in range(1, N*N+1)]
    m = [[0]*N for _ in range(N)]
    l_pos, m_pos = 0, 0
    while m_pos < N:
        r = 0
        while r <= m_pos:
            m[r][m_pos] = l[l_pos]
            l_pos += 1
            r += 1
        c = m_pos-1
        while c >= 0:
            m[m_pos][c] = l[l_pos]
            l_pos += 1
            c -= 1
        m_pos += 1
    return m


T = int(input())
for _ in range(T):
    N = int(input())
    result = solve(N)
    for r in result:
        print(" ".join(map(str, r)))