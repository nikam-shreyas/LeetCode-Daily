# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        double = head
        if head==None:
            return None
        while double and double.next:
            double=double.next.next
            curr=curr.next
        return curr