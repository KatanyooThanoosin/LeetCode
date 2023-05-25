class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        m=1
        if target<nums[0]:
            i=len(nums)-1
            m=-1
        while True:
            if nums[i]==target:return i
            i+=m
            if m==-1:
                if i<0 or nums[i]<target or (i<len(nums)-1 and nums[i]>nums[i+1]):return -1
            else:
                if i==len(nums) or nums[i]>target or (i>0 and nums[i]<nums[i-1]):return -1
