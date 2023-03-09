# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def isCycle(head):
            if head is None:
                return False
            slow = head
            fast = head.next
            while fast is not None and fast.next is not None:
                if fast==slow:
                    return True
                fast = fast.next.next
                slow = slow.next
            return False
        if not isCycle(head):
            return None

        s = set()
        curr = head
        while True:
            if curr in s:
                return curr
            s.add(curr)
            curr=curr.next
        return None
                