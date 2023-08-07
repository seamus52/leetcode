# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 
# time: O(n)
# space O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        
        while head:
            nodes.append(head)
            head = head.next

        # specials case 1: removing the nth node removes all nodes
        if n == 1 and len(nodes) == n:
            return None

        # special case 2: removing the 1st node        
        if len(nodes) == n:
            return nodes[1]

        nodes_retro = [None] # last node of a linked list is None
        for i in range(n):
            nodes_retro.append(nodes.pop())

        nodes_retro.pop()
        if len(nodes) > 0 and len(nodes_retro) > 0:
            nodes[-1].next = nodes_retro[-1]

        return nodes[0]
        
        
