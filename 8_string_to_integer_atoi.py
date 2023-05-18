class Solution:
    def myAtoi(self, s: str) -> int:
        t=""
        i=0
        check=False
        s=s.strip()
        while i<len(s):
            if s[i].isdecimal() or ((s[i]=="+" or s[i]=="-")and not check):
                t+=s[i]
                check=True
            else:
                break
            i+=1
        if t=="" or t=="+" or t=="-":t=0
        else:
            t=int(t)
            if t>2**31-1:
                t=2**31-1
            elif t<-2**31:
                t=-2**31
        return t
