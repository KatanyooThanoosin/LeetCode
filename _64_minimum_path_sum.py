class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:
        m = len(dp)
        n = len(dp[0])
        for i in range(1,n):dp[0][i]+=dp[0][i-1]
        for i in range(1,m):
            dp[i][0]+=dp[i-1][0]
            for j in range(1,n):
                dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
