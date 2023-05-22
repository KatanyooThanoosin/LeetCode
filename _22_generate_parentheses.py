class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:return {}
        elif n==1:return {"()"}
        return self.rc(n-1)
    
    def rc(self,n,t="()"):
        if n==0:return {t}
        s=set()
        for i in range(len(t)+1):
            k=t[:i]+"()"+t[i:]
            if k not in s:
                s=s.union(self.rc(n-1,k))
        return s
