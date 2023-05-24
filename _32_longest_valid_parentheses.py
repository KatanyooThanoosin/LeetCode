class Solution:
    def longestValidParentheses(self, a: str) -> int:
        m=0
        l=[0]
        for i in range(1,len(a)):
            if a[i]=="(":l.append(0)
            else:
                k=0
                if a[i-1]=="(":
                    k=(l[i-2] if i>=2 else 0)+2
                elif i-l[i-1]>0 and a[i-l[i-1]-1]=="(":
                    k=l[i-1] + (l[i-l[i-1]-2] if i-l[i-1]>=2 else 0) + 2
                l.append(k)
                m=max(m,l[-1])
        return m      
