class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[1]if obstacleGrid[0][0]==0 else [0]
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        for i in range(1,n):
            if obstacleGrid[0][i]==0:dp.append(dp[i-1])
            else:dp.append(0)
        dp=[dp]
        for i in range(1,m):
            if obstacleGrid[i][0]==1:dp.append([0])
            else:dp.append([dp[i-1][0]])
            for j in range(1,n):
                if obstacleGrid[i][j]==1:dp[i].append(0)
                else:dp[i].append(dp[i-1][j]+dp[i][j-1])
        return dp[-1][-1]
