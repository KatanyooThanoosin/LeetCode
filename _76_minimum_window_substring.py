class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        need = {}
        for i in t:need[i] = need[i]+1 if i in need else 1
        match = 0
        l = 0
        start = 0
        lenw = len(s) + 1
        
        for r, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                match += need[ch] == 0

            while match == len(need):
                if lenw > r-l+1:
                    start,lenw = l, r-l+1
                
                rem = s[l]
                l+=1
                if rem in need:
                    match -= need[rem] == 0
                    need[rem] +=1 
        return s[start:start+lenw] if lenw <= len(s) else ''
