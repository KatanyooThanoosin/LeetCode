class Solution:
    def removeDuplicates(self,nums):
        i=j=0
        while i<len(nums) and j<len(nums):
            nums[i]=nums[j]
            i+=1
            j+=1
            while j<len(nums) and nums[j-1]==nums[j]:
                j+=1
            
        return i
