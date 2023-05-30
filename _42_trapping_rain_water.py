class Solution:
    def trap(self, h):
        l=0
        r=len(h)-1
        maxL=max(h[l],0)
        maxR=max(h[r],0)
        s=0
        while l<r:
            if maxL>maxR:
                r-=1
                a=min(maxL,maxR)-h[r]
                if a>=0:s+=a
                maxR=max(maxR,h[r])
            else:
                l+=1
                a=min(maxL,maxR)-h[l]
                if a>=0:s+=a
                maxL=max(maxL,h[l])
        return s
