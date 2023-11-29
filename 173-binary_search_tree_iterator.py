# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.nodes.append(root.val)
            dfs(root.right)

        self.ptr = -1
        self.nodes = []
        dfs(root)
        
    def next(self) -> int:
        self.ptr += 1
        return self.nodes[self.ptr]
        
    def hasNext(self) -> bool:
        return self.ptr < len(self.nodes) - 1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
