# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# time O(n) - n = sum of nodes in both lists
# space O(1), no new data item is created, just changing references
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode() # trick 1
        tail = dummy_head # trick2
        curr1 = list1
        curr2 = list2

        while curr1 and curr2: # consider both lists for taking the smaller item
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        if curr1: # pick remaining items from list1
            tail.next = curr1
        if curr2: # pick remaining items from list2
            tail.next = curr2
        
        return dummy_head.next

