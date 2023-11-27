# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        curr = head
        l = 0

        while curr.next:
            l += 1
            curr = curr.next
        
        curr.next = head
        l += 1
        
        if k > l:
            k = k % l

        prev = curr
        for _ in range(l - k + 1):
            prev = curr
            curr = curr.next
        prev.next = None

        return curr
