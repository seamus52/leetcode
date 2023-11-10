# time: O(vertex * time it takes to check subtree)
# space: O(# of vertices of tree + subtree) - at most, # of vertices recursive calls will be made on root. Each time a comparison may be called, but it will not be accumulated (memory will be released immediately)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check for all subtree rooted at all nodes of tree "root"
        def dfs(node):
            # if node is empty, then its tree cannot be identical to the desired
            if node is None:
                return False
            # else it is a potential candidate to check
            elif is_identical(node, subRoot):
                return True

            # if there was no match, check children recursively
            return dfs(node.left) or dfs(node.right)

        def is_identical(node1, node2):
            # If any one Node is empty, both should be empty
            if node1 is None or node2 is None:
                return node1 is None and node2 is None

            # both Nodes value should be equal
            # and their respective left and right subtree should be identical
            return (node1.val == node2.val and
                    is_identical(node1.left, node2.left) and
                    is_identical(node1.right, node2.right))

        # Check for node rooted at "root"
        return dfs(root)
