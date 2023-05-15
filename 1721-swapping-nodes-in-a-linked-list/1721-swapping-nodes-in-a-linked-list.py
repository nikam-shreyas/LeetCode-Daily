# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = head
        end = head
        for _ in range(k-1):
            end = end.next
            begin = begin.next
        last = head
        end = end.next
        while end:
            end = end.next
            last = last.next
        last.val, begin.val = begin.val, last.val
        return head
        