# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=[]
        flag=True
        queue.append(root)
        ans=[]
        while(queue):
            temp=[]
            n=len(queue)
            for i in range(n):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            if flag:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            flag= not flag
            print(flag)
        return ans
