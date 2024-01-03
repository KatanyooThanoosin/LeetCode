class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        c = 1
        i,j = 0,0
        while True:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1
            if c>2:
                c=0
                while j<len(nums) and nums[i]==nums[j]:j+=1
                i-=1
            if j==len(nums):break
            i+=1
            if nums[i-1] < nums[j]:c=1
            else:c+=1       
        return i+1
