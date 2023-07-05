class Solution:
    def simplifyPath(self, path: str) -> str:
        p=path.strip('/').split('/')
        re=[]
        for i in p:
            if i=="" or i==".":continue
            if i=="..":
                re=re[:-1]
            else:
                re.append(i)
        return "/"+"/".join(re)
