# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Partition a linked list around a pivot value x
class Solution:

    # Partition the given linked list head around pivot x
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        # Start at the head of the list 
        current = head  

        # Initialize empty nodes for less than and greater than x lists
        less_head = ListNode()
        less_curr = less_head

        greater_head = ListNode()  
        greater_curr = greater_head

        # Iterate through original list
        while current:

            # If current node is less than x
            if current.val < x:

                # Add to less than list
                less_curr.next = ListNode(current.val)  
                less_curr = less_curr.next

            # If current node is greater than or equal to x  
            else:

                # Add to greater than list
                greater_curr.next = ListNode(current.val)
                greater_curr = greater_curr.next

            # Move to next node in original list  
            current = current.next

        # Join the two partitioned lists
        less_curr.next = greater_head.next 

        # Return new partitioned list
        return less_head.next