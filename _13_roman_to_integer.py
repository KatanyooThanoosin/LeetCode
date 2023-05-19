class Solution:
    def romanToInt(self, s: str) -> int:
        d={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        n=0
        while s!="":
            if len(s)>1 and d[s[1]]>d[s[0]]:
                n+=d[s[1]]-d[s[0]]
                s=s[2:]
            else:
                n+=d[s[0]]
                s=s[1:]
        return n
