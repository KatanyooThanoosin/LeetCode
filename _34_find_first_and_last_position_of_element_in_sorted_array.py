class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1
        ki=1
        kj=-1
        l=[-1,-1]
        while i<=j:
            if nums[i]==target:
                ki=0
                l[0]=i
            if nums[j]==target:
                kj=0
                l[1]=j
            if -1 not in l:break
            i+=ki
            j+=kj
        return l
