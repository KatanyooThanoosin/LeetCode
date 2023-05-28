class Solution:
    def countAndSay(self, n: int) -> str:
        if n<3:return "1"*n
        a=self.countAndSay(n-1)
        n=len(a)
        s=""
        c=1
        for i in range(n):
            if i==n-1 or a[i]!=a[i+1]:
                s+=str(c)+a[i]
                c=1
            else:c+=1
        return s
