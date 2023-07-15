class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=set()
        c=set()
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r.add(i)
                    c.add(j)
        for i in range(n):
            for j in range(m):
                if i in r or j in c:
                    matrix[i][j]=0
