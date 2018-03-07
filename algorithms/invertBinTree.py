# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invertRecursive(node):
            if node == None:
                return None
            temp = node.right
            node.right = node.left
            node.left = temp
            invertRecursive(node.right)
            invertRecursive(node.left)
            return node

        return invertRecursive(root)
        
