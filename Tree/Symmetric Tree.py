# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymcheck(self,left,right):
            if left==None or right==None:
                return left==right
            if left.val != right.val :
                return False
            return self.isSymcheck(left.left,right.right) and self.isSymcheck(left.right,right.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.isSymcheck(root.left,root.right)
        
