# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time O(n) - n = sum of nodes in both lists
# space O(1), no new data item is created, just changing references
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-666)
        tail = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                rest = list1.next
                list1.next = None
                tail.next = list1
                list1 = rest
            else:
                rest = list2.next
                list2.next = None
                tail.next = list2
                list2 = rest
            
            # very important!
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy_head.next
