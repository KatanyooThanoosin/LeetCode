class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.combi(n,k)

    def combi(self, n, k,c=1, path=[]):
        if len(path) == k:return [path]
        l=[]
        for i in range(c,n+1):
            l += self.combi(n,k,i+1,path+[i])
        return l
