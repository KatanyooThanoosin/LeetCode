class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        while len(s)>0 and len(p)>0:
            if len(p)>1 and p[1]=="*":
                while p[0]==s[0] or p[0]==".":
                    s=s[1:]
                    if s=="":
                        break
                p=p[2:]
            else:
                if p[0]!=s[0] and p[0]!=".":
                    return False
                else:
                    p=p[1:]
                    s=s[1:]
        if len(s)>0:
            return False
        return True
