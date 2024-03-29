# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(next = head)
        prev = dummy
        curr = head
        nxt = head.next
        while curr and nxt:
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt
            prev = curr
            curr = curr.next
            if curr and curr.next:
                nxt = curr.next
            else:
                break
        return dummy.next
        