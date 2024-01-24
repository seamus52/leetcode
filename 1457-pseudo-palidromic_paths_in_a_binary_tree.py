# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def is_pseudo_palindrome(nums):
            c = Counter(nums)
            even_cnt = 0
            odd_cnt = 0
            for v in c.values():
                if v % 2 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1

            return odd_cnt == 1 or (even_cnt != 0 and odd_cnt == 0)


        def dfs(root, path):
            nonlocal cnt
            path.append(root.val)

            if not root.left and not root.right:
                # print(path)
                if is_pseudo_palindrome(path):
                    cnt += 1
                path.pop()
                return

            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            path.pop()


        cnt = 0
        dfs(root, [])
        return cnt

