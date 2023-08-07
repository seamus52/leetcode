# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        prev = dummy_head
        
        while head and head.next: # this is the key: no next.next!
            first = head
            second = head.next
            remaining = second.next

            # swap
            # no need to save remaining: second.next is remaining
            # variable added for readability
            prev.next = second
            first.next = remaining
            second.next = first

            # reinitialize for next cycle
            prev = first
            head = first.next

        return dummy_head.next
