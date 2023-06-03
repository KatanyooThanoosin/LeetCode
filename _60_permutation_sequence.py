class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s=""
        l=[str(i) for i in range(1,n+1)]
        f=[1]
        for i in range(2,n):f.append(f[-1]*i)
        k-=1
        while n>1:
            a=k%f[n-2]
            k=k//f[n-2]
            s+=l.pop(k)
            k=a
            n-=1
        return s+l[0]
