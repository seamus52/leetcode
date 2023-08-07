# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# time: O(n*e)
# space: O(tree depth) - recursion stack size
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def countPath(root, remain, isRoot: bool):
            nonlocal cnt
            if not root:
                return

            if isRoot: # 1 complete pass to aggregate exact matches w/ node value
                countPath(root.right, target_sum, True)
                countPath(root.left, target_sum, True)

            remain -= root.val
            if remain == 0:
                cnt += 1
            
            countPath(root.right, remain, False)
            countPath(root.left, remain, False)
            

        cnt = 0
        target_sum = targetSum
        countPath(root, target_sum, True)
        return cnt
    
