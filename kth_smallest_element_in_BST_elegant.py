# time: O(n)
# space: O(depth) -> stack space

# solution matches efficiency of original w/ readability of own
class Solution:
    def kthSmallest(self, root, k):
        def traverse_inorder(root, collector):
            if root:
                traverse_inorder(root.left, collector)
                collector.append(root.val)
                traverse_inorder(root.right, collector)
    
        collector = []
        traverse_inorder(root, collector)
        return collector[k - 1]
