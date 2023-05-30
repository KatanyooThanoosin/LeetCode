class Solution:
    def multiply(self, n1: str, n2: str) -> str:
        s=0
        if n1=="0" or n2=="0":return "0"
        elif n1=="1":return n2
        elif n2=="1":return n1
        for i in n1:
            s*=10
            v=0
            a=ord(i)-ord('0')
            for j in n2:
                v*=10
                b=ord(j)-ord('0')
                v+=a*b
            s+=v
        return str(s)
