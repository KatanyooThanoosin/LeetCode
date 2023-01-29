class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m=0
        for i in range(len(s)):
            tmp=[]
            j=i
            while j<len(s) and s[j] not in tmp:
                tmp+=[s[j]]
                j+=1
            if len(tmp)>m:m=len(tmp)
        return m
