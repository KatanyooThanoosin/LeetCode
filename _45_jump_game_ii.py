class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:return 0
        i=0
        j=nums[0]
        c=0
        while i<len(nums):
            if i+j>=len(nums)-1:return c+1
            i,c=i+1,c+1
            for k in range(i+1,i+j):
                if k-i-1+nums[k]>=nums[i]:i=k
            j=nums[i]
        return c 
