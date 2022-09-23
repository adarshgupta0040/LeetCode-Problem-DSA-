# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def height(self,root):
        if root==None:
            return 0
        
        Lh=self.height(root.left)
        if Lh==-1:
            return -1
        Rh=self.height(root.right)
        if Rh==-1:
            return -1
        
        if abs(Lh-Rh)>1:
            return -1
        return max(Lh,Rh)+1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.height(root)== -1 :      #if height is -1 then False else True
            return False
        return True
