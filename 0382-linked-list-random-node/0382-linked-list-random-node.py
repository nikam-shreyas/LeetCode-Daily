# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        curr = head
        self.n=0
        while curr is not None:
            self.n+=1
            curr=curr.next
        self.ptr = head

    def getRandom(self) -> int:
        skips = random.randint(0, self.n-1)
        curr = self.head
        for i in range(skips):
            curr = curr.next
        return curr.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()