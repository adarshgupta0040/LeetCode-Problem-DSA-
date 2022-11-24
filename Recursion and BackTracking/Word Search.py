class Solution:
    def dfs(self,ind,i,j,board,word):
        if ind == len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) : #out of bound case
            return False
        ans=False
        if word[ind]==board[i][j]:
            board[i][j]="*"
            ans=self.dfs(ind+1,i+1,j,board,word) or self.dfs(ind+1,i,j+1,board,word) or self.dfs(ind+1,i-1,j,board,word) or self.dfs(ind+1,i,j-1,board,word) 
            board[i][j]=word[ind]
        return ans

    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board[0])
        n=len(board)
        ind=0
        for i in range(n):
            for j in range(m):
                if word[ind]==board[i][j] :
                    if self.dfs(ind,i,j,board,word):
                        return True
        return False
      
      
  
# Intuition
Using DFS and Backtracking

# Approach
check if the first char in word present in board or not. if present call DFS functn.
1.firstly if the char reaches the end of word return true.
2.write all edge case of Out of bound condition and return False.
3.Now check if the that char of word present in the board or not. if present then mark that place with star(*) so that it do not go back from that path for further search of char. Call recursively for next char in the word with all direction Up,down,left,right.
4.after all this is done then replace the star with that original char in the board.
5.At Last return ans.

# Complexity
Time complexity: O(4^n * n^2)
Space complexity: O(1)  
  
  
