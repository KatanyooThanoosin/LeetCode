class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=strs[0]
        for i in range(len(strs)):
            while l!=strs[i][:len(l)]:
                l=l[:-1]
                if l=="":return ""
        return l
