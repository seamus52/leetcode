# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time: O(n)
# space: O(n)
# O(1) space is possible with reversing 2nd half
# then use 2 pointers to comare 1st element w/ 1st after half of list, and so on
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        return values == values[::-1]
