# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = head
        if not odds:
            return head
        evens = head.next
        if not evens:
            return head
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
            