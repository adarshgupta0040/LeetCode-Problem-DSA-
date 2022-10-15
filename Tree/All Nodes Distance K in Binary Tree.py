# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def parent(self,root,d,target):
        queue=[]
        d[root]=None
        queue.append(root)
        while(queue):
            node=queue.pop(0)
            if node.left:
                d[node.left]=node
                queue.append(node.left)
            if node.right:
                d[node.right]=node
                queue.append(node.right)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        d={}
        self.parent(root,d,target)
        visited={}
        queue1=[]
        queue1.append(target)
        visited[target]=True
        distance=0
        while(queue1):
            n=len(queue1)
            if distance==k:
                break
            else:
                distance+=1
            for i in range(n):
                curr=queue1.pop(0)
                if curr.left and curr.left not in visited :
                    queue1.append(curr.left)
                    visited[curr.left]=True
                if curr.right and curr.right not in visited :
                    queue1.append(curr.right)
                    visited[curr.right]=True
                if d[curr] and d[curr] not in visited:
                    queue1.append(d[curr])
                    visited[d[curr]]=True
                
        res=[]
        while(queue1):
            curr=queue1.pop(0)
            res.append(curr.val)
        return res
      
      
