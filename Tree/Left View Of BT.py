class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if root==None:
        return []
    d={}
    queue=[]
    queue.append([root,0])
    while(queue):
        data=queue.pop(0)
        node=data[0]
        index=data[1]
        d[index]=node.data
        if node.right:
            queue.append([node.right,index+1])
        if node.left:
            queue.append([node.left,index+1])
    for k,v in d.items():
        queue.append(v)
    return queue
