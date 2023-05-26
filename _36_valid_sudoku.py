class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l=[]
        for i in range(9):
            for j in range(9):
                e=board[i][j]
                if e!=".":
                    if (i,e) in l or(e,j) in l or(i//3,j//3,e)in l:return False
                    l+=[(i,e),(e,j),(i//3,j//3,e)]
        return True
