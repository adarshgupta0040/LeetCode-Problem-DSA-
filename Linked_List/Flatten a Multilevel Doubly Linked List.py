"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        tail=head
        stack=[]
        while(curr!=None):
            if curr.child != None:
                temp=curr.child
                if curr.next !=None:
                    stack.append(curr.next)
                    curr.next.prev=None
                curr.next=temp
                temp.prev=curr
                curr.child=None
            tail=curr
            curr=curr.next
        
        while(stack):
            curr=stack.pop()
            tail.next=curr
            curr.prev=tail
            while(curr!=None):
                tail=curr
                curr=curr.next
            
        return head
