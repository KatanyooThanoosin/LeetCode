class Solution:
    dd = {"2":"abc","3":"def","4":"ghi","5":"jkl", "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        return self.rc(digits,"") if digits!="" else ""

    def rc(self,dg,s):
        if dg=="":return [s]
        l=[]
        for i in self.dd[dg[0]]:
            l+=self.rc(dg[1:],s+i)
        print(l)
        return l
