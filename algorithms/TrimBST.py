# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def find_root(node):
            if node == None:
                return None
            #if current node less than range
            elif(node.val < L):
                return find_root(node.right)
            #if current node greater than range
            elif(node.val > R):
                return find_root(node.left)
            else:
            # if (L <= node.val <= R):
                node.left = find_root(node.left)
                node.right = find_root(node.right)
                return node

        return find_root(root)
            
