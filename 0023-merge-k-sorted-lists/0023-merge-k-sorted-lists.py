# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(l.val, random.random(), l) for l in lists if l is not None]
        heapify(heap)
        ans = ListNode()
        currnode = ans
        while heap:
            currval,_, curr = heappop(heap)
            currnode.next = ListNode(curr.val)
            currnode = currnode.next
            if curr.next:
                heappush(heap, (curr.next.val,random.random(), curr.next))
        return ans.next
            
                 