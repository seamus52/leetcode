# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases
        if not head or k == 0:
            return head

        curr = head
        length = 1
        # measure length of list
        while curr.next:
            curr = curr.next
            length += 1

        # create a cycle
        curr.next = head

        # reduce large k to < length: k % length
        # and express in terms of left rotation
        k = length - (k % length)

        while k > 0:
            curr = curr.next
            k -= 1

        new_head = curr.next
        curr.next = None
        return new_head
