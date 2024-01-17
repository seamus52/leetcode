/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    public TreeNode BuildTree(int[] preorder, int[] inorder)
    {
        
        if (inorder.Length == 0)
        {
            return null;
        }

        TreeNode node = new TreeNode(preorder[0]);
        preorder = preorder.Skip(1).ToArray();
        int inorderIdx = Array.IndexOf(inorder, node.val);

        node.left = BuildTree(preorder.Take(inorderIdx).ToArray(), inorder.Take(inorderIdx).ToArray());
        node.right = BuildTree(preorder.Skip(inorderIdx).ToArray(), inorder.Skip(inorderIdx + 1).ToArray());
        
        return node;
    }
}
