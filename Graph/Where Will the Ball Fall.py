class Solution:
    def dfs(self,i,j,grid):
        if i>=len(grid):
            return j
        if grid[i][j]==1 and j+1<len(grid[0]) and grid[i][j+1]==1 :
            return self.dfs(i+1,j+1,grid)
        elif grid[i][j]==-1 and j-1>=0 and grid[i][j-1]==-1:
            return self.dfs(i+1,j-1,grid)
        elif grid[i][j]==1 and j+1>=len(grid[0]):
            return -1
        else:
            return -1
        
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m=len(grid)
        n=len(grid[0])
        ans=[]
        for i in range(n):
            ans.append(self.dfs(0,i,grid))
        return ans
