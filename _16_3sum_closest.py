class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cl="null"
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                n1,n2,n3 = nums[i],nums[j],nums[k]
                ps=n1+n2+n3
                if cl == "null" or abs(cl-target)>abs(ps-target):
                    cl = ps
                if ps>target:
                    k-=1
                elif ps<target:
                    j+=1
                else:
                    return target
                #while j<k and nums[j]==nums[j-1]:
                    #j+=1
                #while k!=len(nums)-1 and j<k and nums[k]==nums[k+1]:
                    #k-=1
        return cl
