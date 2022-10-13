# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path(self,root,ans,X):            # Root to Node Path
        if root==None:
            return False
        ans.append(root)
        if root.val == X:
            return True
        if self.path(root.left,ans,X) or self.path(root.right,ans,X):
            return True
        ans.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l1,l2=[],[]
        self.path(root,l1,p.val)            
        self.path(root,l2,q.val)
        # print(l1,l2)
        if len(l1)>len(l2):
            k=len(l2)
        else:
            k=len(l1)
        for i in range(k):
            if l1[i]==l2[i]:
                ans=l1[i]
        return ans
