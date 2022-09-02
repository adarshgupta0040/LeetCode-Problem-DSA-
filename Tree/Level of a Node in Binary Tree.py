"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def getLevel(self, root,target):
        if root==None:
            return []
        queue=[]
        ans=[]
        queue.append([root,0])
        while(queue):
            temp=[]
            for i in range(len(queue)):
                data,index=queue.pop(0)
                temp.append(data.data)
                if data.left:
                    queue.append([data.left,index+1])
                if data.right:
                    queue.append([data.right,index+1])
            ans.append(temp)
        for i in range(len(ans)):
            if target in ans[i]:
                return i+1
        return 0
