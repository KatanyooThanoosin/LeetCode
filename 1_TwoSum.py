class Solution(object):
    def twoSum(self, nums, target):
        m={}
        for i in range(len(nums)):
            if target-nums[i] in m:return [m[target-nums[i]],i]
            else:m[nums[i]]=i
