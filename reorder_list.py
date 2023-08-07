# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(n)
# space: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()

        curr = head
        while curr:
            q.append(curr)
            curr = curr.next

        dummy_head = TreeNode(None)
        curr = dummy_head
        while q:
            curr.next = q.popleft()
            if q:
                curr.next.next = q.pop()
                curr.next.next.next = None
                curr = curr.next.next
            else:
                curr.next.next = None
                curr = curr.next

        return dummy_head.next
