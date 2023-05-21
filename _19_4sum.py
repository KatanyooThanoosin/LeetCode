class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s=set()
        n=len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                l=j+1
                r=n-1
                while l<r:
                    n1,n2,n3,n4 =nums[i],nums[j],nums[l],nums[r]
                    k=n1+n2+n3+n4
                    if k>target:
                        r-=1
                    elif k<target:
                        l+=1
                    else:
                        s.add((n1,n2,n3,n4))
                        r-=1
                        l+=1
        return s
