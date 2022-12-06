# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddhead = head
        if not oddhead:
            return None
        evenhead = head.next
        if not evenhead:
            return oddhead
        odd = head
        even = head.next
        while odd and even:
            odd.next=even.next
            if even.next:
                odd=even.next
                even.next=odd.next
                even=odd.next
            else:
                break
        odd.next = evenhead
        return oddhead