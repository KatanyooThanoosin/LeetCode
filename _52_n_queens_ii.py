class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.pm(n)
    
    def pm(self,n,r=0,cl=[],ld=[],rd=[]):
        if r==n:return 1
        a=0
        for i in range(n):
            if i not in cl and i+r not in ld and i-r not in rd:
                a+=self.pm(n,r+1,cl+[i],ld+[i+r],rd+[i-r])
        return a
