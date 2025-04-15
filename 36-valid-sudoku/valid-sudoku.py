class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b=[]
        for i in range (len(board)):
            k=Counter(board[i])
            k.pop('.')
            k=sorted(k.values(),reverse=True)
            if len(k)>0 and k[0]>1:
                return False
            k=[]
            for j in range(len(board)):
                k.append(board[j][i])
            b.append(k)

        for i in range (len(b)):
            k=Counter(b[i])
            k.pop('.')
            k=sorted(k.values(),reverse=True)
            if len(k)>0 and k[0]>1:
                return False
        
        map=[(0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6),]
        
        for i,j in map:
            s=[]
            for row in range(i,i+3):
                for column in range(j,j+3):
                    s.append(board[row][column])
                
                k=Counter(s)
                k.pop('.', None)
                for i in k.values():
                    if i >1:
                        return False
            

        return True
        
        

        return True
        