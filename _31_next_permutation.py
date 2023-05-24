class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=len(nums)-1
        j=i-1
        while j>=0 and nums[j]>=nums[i]:
            i,j=i-1,j-1
        if j>=0:
            while i<len(nums) and nums[i]>nums[j]:i+=1
            i-=1
            nums[i],nums[j]=nums[j],nums[i]
        i=len(nums)-1
        j+=1
        while j<i:
            nums[i],nums[j]=nums[j],nums[i]
            j,i=j+1,i-1
