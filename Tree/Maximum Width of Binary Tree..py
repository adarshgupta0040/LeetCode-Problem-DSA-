# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        queue=[]
        width=0
        queue.append([root,0])
        while(queue):
            n=len(queue)
            level_minvalue=queue[0][1]
            for i in range(n):
                node,index=queue.pop(0)
                curr_index=index-level_minvalue
                if i==0:
                    start_index=curr_index
                if i==n-1:
                    end_index=curr_index
                if node.left:
                    queue.append([node.left,(2*curr_index+1)])
                if node.right:
                    queue.append([node.right,(2*curr_index+2)])
            width=max(width,(end_index-start_index+1))
            # print(width)
        return width
