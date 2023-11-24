# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sentinel = ListNode()
        prev = sentinel

        curr = head
        while curr and curr.next:
            first = curr
            second = curr.next
            rest = second.next

            first.next = rest
            second.next = first

            prev.next = second
            prev = first
            curr = rest

        return sentinel.next

