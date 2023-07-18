class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        k=matrix[(l+r)//2]
        print(k)
        while l<r and (k[0]>target or k[-1]<target):
            if k[0]>target:
                r=(l+r)//2-1
            else:
                l=(l+r)//2+1
            k=matrix[(l+r)//2]
        l=0
        r=len(k)-1
        t=k[(l+r)//2]
        while l<r and t!=target:
            if t>target:
                r=(l+r)//2-1
            else:
                l=(l+r)//2+1
            t=k[(l+r)//2]
        return t==target
