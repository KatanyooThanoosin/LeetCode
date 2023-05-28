class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        if sum(candidates)<target:return []
        return self.rc(candidates,target)
    
    def rc(self,l,t,path=[]):
        r=[]
        if t==0:return [path]
        for i in range(len(l)):
            if i>0 and l[i-1]==l[i]:continue
            if l[i]>t:break
            r+=self.rc(l[i+1:],t-l[i],path+[l[i]])
        return r
