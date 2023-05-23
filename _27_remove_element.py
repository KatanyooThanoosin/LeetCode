class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=j=0
        while i<len(nums) and j<len(nums):
            while j<len(nums) and nums[j]==val:
                j+=1
            if j==len(nums):
                break
            nums[i]=nums[j]
            i+=1
            j+=1
        return i
