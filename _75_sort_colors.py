class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        swI = 0
        while i<len(nums):
            if nums[i]==0:
                nums[i],nums[swI] = nums[swI],nums[i]
                swI+=1
            i+=1
        i=swI
        while i<len(nums):
            if nums[i]==1:
                nums[i],nums[swI] = nums[swI],nums[i]
                swI+=1
            i+=1
