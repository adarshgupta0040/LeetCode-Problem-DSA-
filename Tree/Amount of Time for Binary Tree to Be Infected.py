# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mapParent(self,root,d,start):                       #for mapping with parent node to visit and finding add of start
        queue=[]
        queue.append(root)
        d[root]=None
        while(queue):
            node=queue.pop(0)
            if node.left:
                d[node.left]=node
                queue.append(node.left)
            if node.right:
                d[node.right]=node
                queue.append(node.right)
            if node.val==start:
                tar=node
        return tar
    
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        d={}
        tar=self.mapParent(root,d,start)
        queue=[]
        visited={}
        queue.append(tar)
        visited[tar]=True
        ans=0
        while(queue):
            n=len(queue)
            flag=0
            for i in range(n):
                curr=queue.pop(0)
                if curr.left and curr.left not in visited:
                    flag=1
                    visited[curr.left]=True
                    queue.append(curr.left)
                if curr.right and curr.right not in visited:
                    flag=1
                    visited[curr.right]=True
                    queue.append(curr.right)
                if d[curr] and d[curr] not in visited:
                    flag=1
                    visited[d[curr]]=True
                    queue.append(d[curr])
            if flag:
                ans+=1
        return ans
