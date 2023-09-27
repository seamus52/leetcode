# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(n)
# space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    """
    Do not return anything, modify head in-place instead.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        q = deque()

        curr = head
        while head:
            q.append(head)
            head = head.next
            q[-1].next = None

        dummy_head = ListNode()
        tail = dummy_head
        while len(q) > 1:
            tail.next = q.popleft()
            tail = tail.next
            tail.next = q.pop()
            tail = tail.next

        if q:
            tail.next = q.pop()

        return dummy_head.next

