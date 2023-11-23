# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# collect paths in natural order (copy at end of path)
# insert at the front so that the right view will be favored
# take rightmost path,
# iterate backwards, if the one left is taller, append the delta on top (align correctly)
# further optimization opportunity:
# 1) traverse right first -> no insert(0,..) is necessary
# 2) do not collect all paths, only collect excess path if level == len(view)
# time: O(n)
# space: O(max(h, d) - h = tree height, d = tree diameter recursive call stack
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        paths = []
        self.traverse_and_collect(root, path, paths)
        
        right_view = []
        if len(paths) > 0:
            for p in paths:
                if len(right_view) == 0:
                    right_view = p
                if len(p) > len(right_view):
                    right_view += p[len(right_view):] 
        return right_view

    def traverse_and_collect(self, root, path, paths):
        if not root:
            return

        if not root.left and not root.right:
            path.append(root.val)
            paths.insert(0, path[:])
            path.pop()
            print(paths)
            return
        
        path.append(root.val)
        self.traverse_and_collect(root.left, path, paths)
        self.traverse_and_collect(root.right, path, paths)
        if len(path) > 0:
            path.pop()

