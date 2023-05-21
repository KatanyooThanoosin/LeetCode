class Solution:
    def isValid(self, s: str) -> bool:
        pt = {")":"(","}":"{","]":"["}
        if s[0] in pt:
            return False
        st = [s[0]]
        for i in range(1,len(s)):
            if s[i] in pt:
                if len(st)==0:return False
                if pt[s[i]]==st[0]:
                    st.pop(0)
                else:return False
            else:
                st.insert(0,s[i])
        return len(st)==0
