# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n log n)
# space: O(n)
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        vals.sort()
        sorted_head = ListNode()
        current = sorted_head
        for v in vals:
            current.next = ListNode(v)
            current = current.next

        return sorted_head.next
