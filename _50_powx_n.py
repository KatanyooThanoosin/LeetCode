class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:return 0
        if n<0:return 1/self.p(x,n*-1)
        return self.p(x,n)
    
    def p(self,x,n):
        if n==0:return 1
        if n%2==0:return self.p(x*x,n//2)
        else:return x*self.p(x*x,n//2)
