# https://leetcode.com/contest/weekly-contest-191/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

def maxArea(h, w, hcuts, vcuts):
    hcuts.sort()
    vcuts.sort()
    maxdiffh = hcuts[0]
    for i in range(1, len(hcuts)):
        maxdiffh = max(maxdiffh, hcuts[i]-hcuts[i-1])
        #print(maxdiffh)
    maxdiffh = max(maxdiffh, h-hcuts[-1])
    #print(maxdiffh)
    maxdiffv = vcuts[0]
    for i in range(1, len(vcuts)):
        maxdiffv = max(maxdiffv, vcuts[i]-vcuts[i-1])
        #print(maxdiffv)
    maxdiffv = max(maxdiffv, w-vcuts[-1])
    return (maxdiffh*maxdiffv)%(10**9 + 7)
