# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize prev as terminator (None)
        prev = None
        # iterate through list
        while head:
            # save remaining part of list beyond current
            rest = head.next
            # reverse current node: flip next pointer to prev
            head.next = prev
            # flip is done, make previous pointer point to current
            prev = head
            # advance the current pointer to the first remaining node in the list
            head = rest

            # or, expressed in a more Pyhonic way:
            # curr.next, prev, curr = prev, curr, curr.next

        # returning prev, as head will be None at this point
        return prev
