# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans=0
        queue=[]
        queue.append([root,0])
        while(queue):
            n=len(queue)
            mmin=queue[0][1]
            for i in range(n):
                curr_id=queue[0][1]-mmin
                Node=queue[0][0]
                queue.pop(0)
                if i==0:
                    first=curr_id
                if i==n-1:
                    last=curr_id
                if Node.left:
                    queue.append([Node.left,curr_id*2+1])
                if Node.right:
                    queue.append([Node.right,curr_id*2+2])  
            ans=max(ans,last-first+1)
        return ans
