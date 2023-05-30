class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p)>0:
            i=1
            k=p[0]
            while i<len(p):
                if p[i]=="*" and p[i-1]=="*":
                    i+=1
                    continue
                k+=p[i]
                i+=1
            p=k
        dp=[[True]+[False]*len(p)]
        if len(p)>0 and p[0]=="*":dp[0][1]=True
        for i in range(len(s)):
            dp.append([False])
            for j in range(len(p)):
                if "?"==p[j] or s[i]==p[j]:
                    dp[i+1].append(dp[i][j])
                elif p[j]=="*":
                    dp[i+1].append(dp[i+1][j] or dp[i][j+1])
                else:
                    dp[i+1].append(False)     
        return dp[-1][-1]
