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
    public int WidthOfBinaryTree(TreeNode root)
    {
        int maxWidth = 0;
        Queue<Tuple<TreeNode, int>> q = new();
        q.Enqueue(new (root, 0));

        while (q.Count() > 0)
        {
            int num_nodes_on_level = q.Count();
            List<int> level = new();

            for (int i = 0; i < num_nodes_on_level; i++)
            {
                var (node, pos) = q.Dequeue();
                level.Add(pos);

                if (node.left != null)
                {
                    q.Enqueue(new (node.left, 2 * pos));
                }

                if (node.right != null)
                {
                    q.Enqueue(new (node.right, 2 * pos + 1));
                }
            }

            // maxWidth = Math.Max(maxWidth, level.Max() - level.Min() + 1);
            maxWidth = Math.Max(maxWidth, level[level.Count() - 1] - level[0] + 1);
        }

        return maxWidth;
    }
}
