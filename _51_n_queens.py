class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.pm(n)
    
    def pm(self,n,r=0,b=[],cl=[],ld=[],rd=[]):
        if r==n:return [b]
        a=[]
        for i in range(n):
            if i not in cl and i+r not in ld and i-r not in rd: 
                nr="."*(i)+"Q"+"."*(n-i-1)
                a+=self.pm(n,r+1,b+[nr],cl+[i],ld+[i+r],rd+[i-r])
        return a
