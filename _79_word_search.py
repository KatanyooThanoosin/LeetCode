class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def ws(i,j,w,b):
            if len(w)==0:return True
        
            if i!=0 and b[i-1][j] == w[0]:
                last,b[i][j] = b[i][j],"_"
                r = ws(i-1,j,w[1:],b)
                b[i][j]=last
                if r:return True
            if i!=len(b)-1 and b[i+1][j] == w[0]:
                last,b[i][j] = b[i][j],"_"
                r = ws(i+1,j,w[1:],b)
                b[i][j]=last
                if r:return True
            if j!=0 and b[i][j-1] == w[0]:
                last,b[i][j] = b[i][j],"_"
                r = ws(i,j-1,w[1:],b)
                b[i][j]=last
                if r:return True
            if j!=len(b[i])-1 and b[i][j+1] == w[0]:
                last,b[i][j] = b[i][j],"_"
                r = ws(i,j+1,w[1:],b)
                b[i][j]=last
                if r:return True
            return False

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y]==word[0]:
                    k = ws(x,y,word[1:],board)
                    if k:return True
                    print("==========================")
        return False
