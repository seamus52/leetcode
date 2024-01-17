/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public string serialize(TreeNode root)
    {
        StringBuilder rser(TreeNode node, StringBuilder s)
        {
            if (node == null) {
                s.Append("null,");
                return s;
            }

            s.Append(node.val + ",");
            s = rser(node.left, s) ;
            s = rser(node.right, s) ;

            return s;
        }

        var sb = rser(root, new());
        return sb.ToString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(string data)
    {
        TreeNode rdeser(Queue<string> nodes)
        {
            if (nodes.Count() == 0)
            {
                return null;
            }

            string val = nodes.Dequeue();
            if (val == "null")
            {
                return null;
            }
            
            TreeNode node = new(Convert.ToInt32(val));

            node.left = rdeser(nodes);
            node.right = rdeser(nodes);

            return node;
        }

        Queue<string> nodesPreorder = new(data.Split(","));

        return rdeser(nodesPreorder);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
