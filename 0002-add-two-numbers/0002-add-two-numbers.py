# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_out = ListNode()
        ans = l_out
        carry = 0
        while l1 and l2:
            l_sum = l1.val+l2.val+carry
            carry = 0
            if l_sum>9:
                carry=1
                l_sum=l_sum%10
            l_out.next = ListNode(l_sum)
            l1=l1.next
            l2=l2.next
            l_out = l_out.next
            
        while l1:
            l_sum = l1.val+carry
            carry = 0
            if l_sum>9:
                carry=1
                l_sum=l_sum%10
            l_out.next = ListNode(l_sum)
            l1=l1.next
            l_out = l_out.next
            
        while l2:
            l_sum = l2.val+carry
            carry = 0
            if l_sum>9:
                carry=1
                l_sum=l_sum%10
            l_out.next = ListNode(l_sum)
            l2=l2.next
            l_out = l_out.next
        
        if carry:
            l_out.next = ListNode(1)
            
        return ans.next