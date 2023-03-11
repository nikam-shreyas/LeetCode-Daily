# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    root = None
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        self.root = None
        def insert(val):
            curr = self.root
            if self.root is None:
                self.root = TreeNode(val=val)
            else:
                while True:
                    # print('in while')
                    if val<curr.val:
                        if curr.left is None:
                            curr.left=TreeNode(val)
                            break
                        else:
                            curr=curr.left
                    else:
                        if curr.right is None:
                            curr.right = TreeNode(val)
                            break
                        else:
                            curr = curr.right
                        
        def recurse(i, j):
            # print('in recurse', i, j)
            if i<0 or j<0 or i>=len(arr) or j>=len(arr) or i>j:
                return
            if i==j:
                insert(arr[i])
            else:
                mid = i+(j-i)//2
                insert(arr[mid])
                recurse(i, mid-1)
                recurse(mid+1, j)
        recurse(0, len(arr)-1)
        return self.root