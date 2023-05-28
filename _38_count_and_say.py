class Solution:
    def countAndSay(self, n: int) -> str:
        if n<3:return "1"*n
        a=self.countAndSay(n-1)
        s=""
        i=1
        c=int("1"+a[0])
        while i<len(a):
            if c%10 == int(a[i]):
                c+=10
            else:
                s+=str(c)
                c=int("1"+a[i])
            i+=1
        return s+str(c)
