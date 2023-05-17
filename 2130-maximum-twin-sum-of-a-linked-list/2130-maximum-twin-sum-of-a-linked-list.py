# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        elements = []
        cur = head
        while cur:            
            elements.append(cur.val)
            cur = cur.next
        maxsum = elements[0]+elements[-1]
        for i in range(len(elements)//2):
            maxsum = max(maxsum, elements[i]+elements[-(i+1)])
        return maxsum
        