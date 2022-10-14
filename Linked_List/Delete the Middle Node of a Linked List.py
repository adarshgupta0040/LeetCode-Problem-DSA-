# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next :
            return 
        hare , tortoise = head.next , head
        while hare.next and hare.next.next :
            hare = hare.next.next 
            tortoise = tortoise.next
        tortoise.next = tortoise.next.next
        return head
