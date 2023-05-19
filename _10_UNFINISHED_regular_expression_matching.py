class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d=[]
        for i in range(len(s)+1):
            d.append([])
            for j in range(len(p)+1):
                if i==0:
                    if j==0:d[i].append(True)
                    elif p[j-1]=="*":d[i].append(d[i][j-2])
                    else:d[i].append(False)
                elif j==0:
                    d[i].append(False)
                elif s[i-1]==p[j-1] or p[j-1]==".":
                    d[i].append(d[i-1][j-1])
                elif p[j-1]=="*":
                    if d[i][j-2]:d[i].append(d[i][j-2])
                    elif s[i-1]==p[j-2] or p[j-2]==".":
                        d[i].append(d[i-1][j])
                    else:d[i].append(False)
                else:
                    d[i].append(False)
        return d[i][j]
