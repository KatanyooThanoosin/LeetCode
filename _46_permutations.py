class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.pm(nums)

    def pm(self,l,path=[]):
        if len(l)==0:return [path]
        a=[]
        for i in range(len(l)):
            l[0],l[i]=l[i],l[0]
            a+=self.pm(l[1:],path+[l[0]])
            l[0],l[i]=l[i],l[0]
        return a
