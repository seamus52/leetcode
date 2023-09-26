"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        if not head:
            return None

        while head:
            nodes[head] = Node(head.val) # k: old node, v: new node
            head = head.next

        prev = None
        for old_node, new_node in nodes.items():
            # setting up next for new node
            if prev:
                prev.next = new_node
            prev = new_node

            # setting up random ptr for new node
            if old_node.random:
                new_node.random = nodes[old_node.random]
            else:
                new_node.random = None

        return list(nodes.values())[0]
        
