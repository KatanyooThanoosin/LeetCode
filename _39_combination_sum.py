class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.rc(target,candidates)

    def rc(self,t,l,i=0,s=0,path=[]):
        if s>t or i==len(l):return
        if s==t:return [path]
        k=[]
        a=self.rc(t,l,i+1,s,path)
        if a:k+=a
        b=self.rc(t,l,i,s+l[i],path+[l[i]])
        if b:k+=b
        return k
