class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        i=0
        j=len(height)-1
        while i<j:
            m=max(m,min(height[i],height[j])*(j-i))
            if height[i] <= height[j]:
                b=i
                i+=1
                while i<j and height[b]>=height[i]:
                    i+=1
            else:
                b=j
                j-=1
                while i<j and height[b]>=height[j]:
                    j-=1
        return m
