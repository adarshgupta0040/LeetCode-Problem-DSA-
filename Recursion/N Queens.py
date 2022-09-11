class Solution:
    def isSafe(self,row,col,board,n):
        x=row
        y=col
        while(y>=0):
            if board[x][y]=="Q":
                return False
            y-=1
        x=row
        y=col
        while(x>=0 and y>=0):
            if board[x][y]=="Q":
                return False
            x-=1
            y-=1
        x=row
        y=col
        while(x<n and y>=0):
            if board[x][y]=="Q":
                return False
            x+=1
            y-=1
        return True
        
        
    def f(self,col,ans,board,n):
        if col==n:
            curr = []
            for m in board:
                curr.append("".join(i for i in m))
            ans.append(curr)
            return
        
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col]="Q"
                self.f(col+1,ans,board,n)
                board[row][col]="."
                
                
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)]for j in range(n)]
        ans=[]
        self.f(0,ans,board,n)
        return ans
      
