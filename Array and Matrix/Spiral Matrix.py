class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        m=len(a)
        n=len(a[0])
        top=0
        down=m-1
        left=0
        right=n-1
        direction=0
        ans=[]
        while(top<=down and left<=right):
            if direction==0:
                for i in range(left,right+1):
                    ans.append(a[top][i])
                top+=1
            if direction==1:
                for i in range(top,down+1):
                    ans.append(a[i][right])
                right-=1
            if direction==2:
                for i in range(right,left-1,-1):
                    ans.append(a[down][i])
                down-=1
            if direction==3:
                for i in range(down,top-1,-1):
                    ans.append(a[i][left])
                left+=1
            direction=(direction+1)%4
        return ans
       
