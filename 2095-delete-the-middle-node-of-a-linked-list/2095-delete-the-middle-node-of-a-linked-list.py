# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = curr
        fast = curr
        if not head.next or not head:
            return None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head