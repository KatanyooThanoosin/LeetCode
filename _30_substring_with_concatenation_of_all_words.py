class Solution:
    def findSubstring(self, l: str, words: List[str]) -> List[int]:
        n=len(words[0])
        nw=len(words)
        t=[]
        ans=[]
        for i in range(len(l)-len(words)+1):
            j=i
            while j<len(l) and j<(nw+i)*n and l[j:j+n] in words:
                t.append(words.pop(words.index(l[j:j+n])))
                j+=n
            if j-i==nw*n:
                ans.append(i)
            words+=t
            t=[]
        return ans
