# Definition for singly-linked list.
# solution: keep track of nodes already seen
# time: O(n)
# space: O(n)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False


