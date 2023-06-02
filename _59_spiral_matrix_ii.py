class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0]*n for _ in range(n)]
        k=1
        t,b,l,r=0,n-1,0,n-1
        while t<=b and l<=r:
            for i in range(l,r+1):
                m[t][i]=k
                k+=1
            t+=1
            for i in range(t,b+1):
                m[i][r]=k
                k+=1
            r-=1
            for i in range(r,l-1,-1):
                m[b][i]=k
                k+=1
            b-=1
            for i in range(b,t-1,-1):
                m[i][l]=k
                k+=1
            l+=1
        return m
