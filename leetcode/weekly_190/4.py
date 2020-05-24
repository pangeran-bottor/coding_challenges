# https://leetcode.com/contest/weekly-contest-190/problems/max-dot-product-of-two-subsequences/

def max_dot_product(nums1, nums2):
    if max(nums1)<0<min(nums2):return max(nums1)*min(nums2)
    if max(nums2)<0<min(nums1):return max(nums2)*min(nums1)
    
    n, m = len(nums1), len(nums2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(
                dp[i][j+1],
                dp[i+1][j],
                dp[i][j] + nums1[i]*nums2[j]
            )
    return dp[n][m]