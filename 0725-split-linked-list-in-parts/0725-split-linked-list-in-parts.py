# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        curr = head
        n = 0
        while curr:
            n+=1
            curr = curr.next
        curr = head
        for i in range(k, 0, -1):
            if n==0:
                ans.append(None)
                continue
            listlen = ceil(n/i)
            n-=listlen            
            newHead = ListNode(curr.val)
            newCurr = newHead
            for j in range(listlen-1):
                newCurr.next = ListNode(curr.next.val)
                curr = curr.next
                newCurr = newCurr.next
            ans.append(newHead)
            curr = curr.next
        return ans
                    
            