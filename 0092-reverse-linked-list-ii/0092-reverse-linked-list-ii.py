# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head
        
        def reverse(curr, n):
            
            if not curr:
                return None
            if n==1:
                return curr
            st = []
            temp = curr
            for i in range(n):
                st.append(temp)
                temp = temp.next
            nxt = temp
            nhead = ListNode()
            temp = nhead
            while st:
                temp.next = ListNode(st.pop().val)
                temp = temp.next
            temp.next = nxt
            
            return nhead.next
        curr = head
        if left==1:
            head = reverse(curr, right-left+1)
        else:
            prev = head
            for i in range(left-1):
                prev = curr
                curr=curr.next            
            prev.next = reverse(curr, right-left+1)
        return head