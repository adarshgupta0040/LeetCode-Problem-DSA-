# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi=float("-inf")
    def maxsum(self,root):
        if root==None:
            return 0
        LH=max(0,self.maxsum(root.left))
        if LH<0:
            LH=0
        RH=max(0,self.maxsum(root.right))
        if RH<0:
            RH=0
        self.maxi=max(self.maxi,(root.val+LH+RH))
        return root.val+max(LH,RH)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum(root)
        return self.maxi
