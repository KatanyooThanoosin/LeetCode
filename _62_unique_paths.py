class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n]+[[1]+[0]*(n-1)for i in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
