# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odds = head
        evens = head.next
        store = evens
        o = odds
        e = evens
        while odds and evens:
            odds.next = evens.next
            odds = odds.next
            if odds:
                evens.next = odds.next
                evens = evens.next
        if evens:
            evens.next = None
        while o and e:
            enext = e.next
            e.next = o
            e = enext
            if e:
                onext = o.next
                o.next = e
                o = onext
        return store
            