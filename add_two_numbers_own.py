# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(N)
# space: O(N)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1_digits = []
        n2_digits = []

        # compose numbers
        while l1:
            n1_digits.insert(0, str(l1.val))
            l1 = l1.next

        while l2:
            n2_digits.insert(0, str(l2.val))
            l2 = l2.next

        n1 = int("".join(n1_digits))
        n2 = int("".join(n2_digits))

        # write result into list
        s = n1 + n2
        dummy_head = ListNode()
        curr = dummy_head
        for d in str(s)[::-1]:
            curr.next = ListNode(d)
            curr = curr.next

        return dummy_head.next
