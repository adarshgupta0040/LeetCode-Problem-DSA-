                                                   #### Preorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self,root,ans):
        if root==None:
            return
        ans.append(root.val)
        self.preorder(root.left,ans)
        self.preorder(root.right,ans)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.preorder(root,ans)
        return ans
        
        
                                                  ### Inorder
          
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,ans):
        if root == None:
            return
        self.inorder(root.left,ans)
        ans.append(root.val)
        self.inorder(root.right,ans)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.inorder(root,ans)
        return ans
      
      
                                                ### Postorder
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderP(self,root,ans):
        if root==None:
            return
        self.postorderP(root.left,ans)
        self.postorderP(root.right,ans)
        ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.postorderP(root,ans)
        return ans
        
        
        
