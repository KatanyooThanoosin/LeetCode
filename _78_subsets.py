class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.ss(nums)

    def ss(self,nums,c=0,path=[]):
        if c==len(nums): return [path]
        return self.ss(nums,c+1, path)+self.ss(nums, c+1,path+[nums[c]])
