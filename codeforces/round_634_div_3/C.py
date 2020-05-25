def solve(n, a):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    
    freq = {}
    for num in a:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    
    if len(freq) == n:
        return 1
    
    freqlist = [(key, freq[key]) for key in freq]
    freqlist.sort(key=lambda x: -x[1])
    
    max_x = 0
    for f in freqlist:
        el = f[0]
        count = f[1]

        freq[el] -= min(count, n//2)

        team2_count = min(count, n//2)
        team1_count = 0
        for key in freq:
            if freq[key] > 0:
                team1_count += 1
        curr_count = min(team1_count, team2_count)
        max_x = max(max_x, curr_count)
        
        freq[el] += min(count, n//2)
    return max_x
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(n, a)
    print(result)