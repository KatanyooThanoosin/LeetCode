class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.ss(0,0,board)
    
    def ss(self,i,j,b):
        if j==9:
            j=0
            i+=1
            if i==9:return True
        if b[i][j]!=".":return self.ss(i,j+1,b)
        for x in range(1,10):
            x=str(x)
            if self.cp(b,i,j,x):
                b[i][j]=x
                if self.ss(i,j+1,b):return True
        b[i][j]="."
        return False

    def cp(self,b,i,j,x):
        if x in b[i]:return False
        for e in b:
            if x==e[j]:return False
        for p in range(3):
            for q in range(3):
                if x == b[(i//3)*3+p][(j//3)*3+q]:return False
        return True
