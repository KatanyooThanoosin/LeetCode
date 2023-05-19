class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s=set()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                n1,n2,n3 = nums[i],nums[j],nums[k]
                ps=n1+n2+n3
                if ps > 0:
                    k-=1
                elif ps < 0:
                    j+=1
                else:
                    s.add((n1,n2,n3))
                    j,k=j+1,k-1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return s
