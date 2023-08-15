# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode()
        curr1 = head1
        head2 = ListNode()
        curr2 = head2
        curr = head
        while curr:
            if curr.val<x:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
            curr = curr.next
        curr1.next = head2.next
        return head1.next