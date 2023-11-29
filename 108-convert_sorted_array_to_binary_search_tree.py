# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(n) every element processed 1x
# space: O(log n) recursive stack - since tree is height-balanced
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return TreeNode()

        mid_idx = len(nums) // 2
        print(mid_idx, nums)
        root = TreeNode(nums[mid_idx], self.sortedArrayToBST(nums[:mid_idx]), self.sortedArrayToBST(nums[mid_idx + 1:]))

        return root
