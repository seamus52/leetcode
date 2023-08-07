# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# create dummy head node
# keep track of tail (as marker of insertion point)
# return dumm.next at the end
# take node with minimum val from lists, advance list element to its next
# stop if lists only has None-s
# create a min_node -> index of node function
# n = number of nodes
# k = number of lists
# time: O(n*k)
# space: O(1) - consuming the original lists
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head

        min_node_idx = self.min_node_idx(lists)
        while min_node_idx != -1:
            # print(lists[min_node_idx])
            tail.next = lists[min_node_idx]
            lists[min_node_idx] = lists[min_node_idx].next
            tail = tail.next

            min_node_idx = self.min_node_idx(lists)

        return dummy_head.next


    def min_node_idx(self, lists):
        min_node = ListNode(float("inf"))
        min_node_idx = -1
        for i, node in enumerate(lists):
            if node:
                if node.val < min_node.val:
                    min_node = node
                    min_node_idx = i

        return min_node_idx


    # optimal solution
    def optimalMergeKLists(self, lists):
        head = tail = ListNode()
        q = PriorityQueue()
        # consume all nodes, populate priority queue
        for l in lists:
            if l:
                q.put((l.val, l))

        # build sorted list by getting elements from priority queue in sorted order
        while not q.empty():
            val, node = q.get()
            tail.next = ListNode(val)
            tail = tail.next
            # list advances, new node is put back to the priority queue so that it can come out upon get in the correct order
            node = node.next
            if node:
                q.put((node.val, node))

        return head.next
