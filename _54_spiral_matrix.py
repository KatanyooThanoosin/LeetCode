class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=[]
        while len(matrix)>0:
            l+=matrix.pop(0)
            if len(matrix)==0:return l
            i=0
            while i<len(matrix)and len(matrix[i])>0:
                l.append(matrix[i].pop())
                i+=1
            l+=matrix.pop()[::-1]
            if len(matrix)==0:return l
            i=len(matrix)-1
            while i>0 and len(matrix[i])>0:
                l.append(matrix[i].pop(0))
                i-=1
        return l
