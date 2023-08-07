# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time: O(n)
# space: O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode(-1)
        curr_odd = odd_dummy
        even_dummy = ListNode(-2)
        curr_even = even_dummy

        i = 1
        while head:
            remaining = head.next
            head.next = None # detach node from remaining list
            
            if i % 2 == 1:
                curr_odd.next = head
                curr_odd = curr_odd.next
            else:
                curr_even.next = head
                curr_even = curr_even.next

            head = remaining
            i += 1

        curr_odd.next = even_dummy.next

        return odd_dummy.next
                

