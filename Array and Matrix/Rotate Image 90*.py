class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(a)):             #transpose then reverse each row
            for j in range(i+1,len(a)):
                a[i][j],a[j][i]=a[j][i],a[i][j]
        
        for i in range(len(a)):
            a[i]=a[i][::-1]
