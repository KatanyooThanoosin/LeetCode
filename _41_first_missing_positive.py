class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        for i in range(1,1000000):
            if i not in nums:return i
