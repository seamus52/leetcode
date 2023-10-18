# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(head):
            if not head or not head.next:
                return head

            first = head
            second = head.next

            first.next = swap(second.next)  # second.next is rest
            second.next = first

            return second

        return swap(head)
