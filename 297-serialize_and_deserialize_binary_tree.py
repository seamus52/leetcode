# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rser(root, serialized):
            if not root:
                serialized += "None,"
                return serialized

            serialized += str(root.val) + ","
            serialized = rser(root.left, serialized)
            serialized = rser(root.right, serialized)
            
            # print(serialized)
            return serialized

        return rser(root, "")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values_preorder = data.split(",")
        def rdeser(values_preorder):
            if values_preorder[0] == "None":
                values_preorder.pop(0)
                return None
            
            root = TreeNode(values_preorder.pop(0))
            root.left = rdeser(values_preorder)
            root.right = rdeser(values_preorder)

            return root

        return rdeser(values_preorder)
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
