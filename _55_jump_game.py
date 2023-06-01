class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=len(nums)-1
        while i>0:
            g=i
            i-=1
            while i>=0 and i+nums[i]<g:
                i-=1
        return True if i==0 else False
