# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertRecursive(node, sum):
            if node == None:
                return sum
            if node.right == None:
                node.val += sum
            else:
                node.val += convertRecursive(node.right, sum)
            return convertRecursive(node.left, node.val)
        convertRecursive(root, 0)
        return root




        
