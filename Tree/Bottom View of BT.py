#User function Template for python3
from collections import OrderedDict

class Solution:
    def bottomView(self, root):
        d={}
        if root==None:
            return []
        queue=[]
        queue.append([0,root])
        while(queue):
            index,node=queue.pop(0)
            d[index]=node.data
            if node.left:
                queue.append([index-1,node.left])
            if node.right:
                queue.append([index+1,node.right])
        dict1 = OrderedDict(sorted(d.items()))
        for k,v in dict1.items():
            queue.append(v)
        return queue
