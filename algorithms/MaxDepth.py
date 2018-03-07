# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def recurDepth(node, depth):
            if(node == None):
                return depth
            return max(recurDepth(node.right, depth+1), recurDepth(node.left, depth +1))
        return recurDepth(root, 0)

        
