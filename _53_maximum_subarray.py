class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m,cur=float('-inf'),0
        for i in range(len(nums)):
            cur += nums[i]
            m = max(cur,m)
            cur = max(cur,0)
        return m
