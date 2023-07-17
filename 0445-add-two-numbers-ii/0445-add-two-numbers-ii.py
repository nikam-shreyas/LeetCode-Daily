# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        curr = l1
        while curr:
            num1=num1*10+curr.val
            curr = curr.next
        curr = l2
        while curr:
            num2 = num2*10+curr.val
            curr = curr.next
        numsum = list(str(num1+num2))
        curr = ListNode()
        head = curr
        for num in numsum:
            curr.next = ListNode(int(num))
            curr = curr.next
        return head.next
            
        