class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=[]
        for i in range(numRows):
            if i==0 or i==numRows-1:
                if 2*numRows-2<=0:
                    l.append(s[i:])
                else:
                    l.append(s[i::2*numRows-2])
            else:
                t=""
                for j in range(i,len(s),2*numRows-2):
                    t+=s[j]
                    if j+2*numRows-2-2*i<len(s):
                       t+=s[j+2*numRows-2-2*i]
                l.append(t)
        return "".join(l)
