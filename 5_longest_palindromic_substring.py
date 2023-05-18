class Solution:
    def longestPalindrome(self, s: str) -> str:
        mt=""
        for i in range(len(s)):
            tmp=s[i]
            for j in range(i+1,len(s)):
                tmp+=s[j]
                if tmp==tmp[::-1] and len(tmp)>len(mt):mt=tmp
            if tmp==tmp[::-1] and len(tmp)>len(mt):mt=tmp
        return mt
